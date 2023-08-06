#!/usr/bin/env python3

"""
.. module:: txnameObj
   :synopsis: Holds the classes and methods used to read and store the
              information in the txname.txt files.
              Also contains the interpolation methods.

.. moduleauthor:: Veronika Magerl <v.magerl@gmx.at>
.. moduleauthor:: Andre Lessa <lessa.a.p@gmail.com>
.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>

"""

import os,sys
from smodels.tools.physicsUnits import GeV, fb, TeV, pb
from smodels.theory.particleNames import elementsInStr
from smodels.tools.stringTools import concatenateLines
from smodels.theory.element import Element
from smodels.theory.topology import TopologyList
from smodels.tools.smodelsLogging import logger
from smodels.experiment.exceptions import SModelSExperimentError as SModelSError
from smodels.tools.caching import _memoize
from scipy.linalg import svd
import scipy.spatial.qhull as qhull
import numpy as np
import unum
import copy
import math
from math import floor, log10


class TxName(object):
    """
    Holds the information related to one txname in the Txname.txt
    file (constraint, condition,...) as well as the data.
    """

    def __init__(self, path, globalObj, infoObj ):
        self.path = path
        self.globalInfo = globalObj
        self._infoObj = infoObj
        self.txnameData = None
        self.txnameDataExp = None ## expected Data
        self._topologyList = TopologyList()

        logger.debug('Creating object based on txname file: %s' %self.path)
        #Open the info file and get the information:
        if not os.path.isfile(path):
            logger.error("Txname file %s not found" % path)
            raise SModelSError()
        txtFile = open(path,'r')
        txdata = txtFile.read()
        txtFile.close()
        if not "txName" in txdata: raise TypeError
        if not 'upperLimits' in txdata and not 'efficiencyMap' in txdata:
            raise TypeError
        content = concatenateLines (  txdata.split("\n") )

        #Get tags in info file:
        tags = [line.split(':', 1)[0].strip() for line in content]
        data = None
        expectedData = None
        dataType = None
        for i,tag in enumerate(tags):
            if not tag: continue
            line = content[i]
            value = line.split(':',1)[1].strip()
            if tags.count(tag) != 1:
                logger.info("Duplicated field %s found in file %s" \
                             % (tag, self.path))
            if ';' in value: value = value.split(';')
            if tag == 'upperLimits' or tag == 'efficiencyMap':
                data = value
                dataType = tag
            elif tag == 'expectedUpperLimits':
                expectedData = value
                dataType = 'upperLimits'
            else:
                self.addInfo(tag,value)

        ident = self.globalInfo.id+":"+dataType[0]+":"+ str(self._infoObj.dataId)
        ident += ":" + self.txName
        self.txnameData = TxNameData( data, dataType, ident )
        if expectedData:
            self.txnameDataExp = TxNameData( expectedData, dataType, ident )

        #Builds up a list of elements appearing in constraints:
        elements = []
        if hasattr(self,'constraint'):
            elements += [Element(el) for el in elementsInStr(str(self.constraint))]
        if hasattr(self,'condition') and self.condition:
            conds = self.condition
            if not isinstance(conds,list): conds = [conds]
            for cond in conds:
                for el in elementsInStr(str(cond)):
                    newEl = Element(el)
                    if not newEl in elements: elements.append(newEl)

        # Builds up TopologyList with all the elements appearing in constraints
        # and conditions:
        for el in elements:
            self._topologyList.addElement(el)

    def hasOnlyZeroes ( self ):
        ozs = self.txnameData.onlyZeroValues()
        if self.txnameDataExp:
            e_ozs = self.txnameDataExp.onlyZeroValues()
            if ozs and e_ozs:
                return True
            if (ozs and not e_ozs) or (e_ozs and not ozs):
                logger.warning ( "%s is weird. One of the (expected, observed) results is zeroes-only, the other one isnt." )
                return False
        return ozs


    def __str__(self):
        return self.txName

    def __lt__ ( self, other ):
        """ sort by txName """
        return self.txName < other.txName

    def getValueFor(self,massarray,expected=False ):
        """ 
        Access txnameData and txnameDataExp to get value for 
        massarray.

        :param massarray: mass array values (with units), i.e.
                          [[100*GeV,10*GeV],[100*GeV,10*GeV]]
        :param expected: query self.txnameDataExp
        """
        if not expected:
            return self.txnameData.getValueFor( massarray )
        else:
            if not self.txnameDataExp:
                return None
            else:
                return self.txnameDataExp.getValueFor( massarray )


    def addInfo(self,tag,value):
        """
        Adds the info field labeled by tag with value value to the object.
        
        :param tag: information label (string)
        :param value: value for the field in string format
        """

        if tag == 'constraint' or tag == 'condition':
            if isinstance(value,list):
                value = [val.replace("'","") for val in value]
            else: value = value.replace("'","")

        try:
            setattr(self,tag,eval(value, {'fb' : fb, 'pb' : pb, 'GeV' : GeV, 'TeV' : TeV}))
        except SyntaxError:
            setattr(self,tag,value)
        except NameError:
            setattr(self,tag,value)
        except TypeError:
            setattr(self,tag,value)

    def getInfo(self, infoLabel):
        """
        Returns the value of info field.
        
        :param infoLabel: label of the info field (string). It must be an attribute of
                          the TxNameInfo object
        """

        if hasattr(self,infoLabel): return getattr(self,infoLabel)
        else: return False

    def hasElementAs(self,element):
        """
        Verify if the conditions or constraint in Txname contains the element.
        Check both branch orderings.
        
        :param element: Element object
        :return: A copy of the element on the correct branch ordering appearing
                in the Txname constraint or condition.
        """

        for el in self._topologyList.getElements():
            if element.particlesMatch(el,branchOrder=True):
                return element.copy()
            else:
                elementB = element.switchBranches()
                if elementB.particlesMatch(el,branchOrder=True):
                    return elementB
        return False

    def hasLikelihood ( self ):
        """ can I construct a likelihood for this map? 
        True for all efficiency maps, and for upper limits maps
        with expected Values. """
        if self._infoObj.dataType == "efficiencyMap":
            return True
        if self.txnameDataExp != None:
            return True
        return False

    def getEfficiencyFor(self,mass):
        """
        For upper limit results, checks if the input mass falls inside the
        upper limit grid.  If it does, returns efficiency = 1, else returns
        efficiency = 0.  For efficiency map results, checks if the mass falls
        inside the efficiency map grid.  If it does, returns the corresponding
        efficiency value, else returns efficiency = 0.

        :param element: Element object
        :return: efficiency (float)
        """

        #Check if the element appears in Txname:
        val = self.txnameData.getValueFor(mass)
        if type(val) == type(fb):
            return 1.  #The element has an UL, return 1
        elif val is None or math.isnan(val):
            return 0.  #The element mass is outside the data grid
        elif type(val) == type(1.):
            return val  #The element has an eff
        else:
            logger.error("Unknown txnameData value: %s" % (str(type(val))))
            raise SModelSError()

class TxNameData(object):
    """
    Holds the data for the Txname object.  It holds Upper limit values or efficiencies.
    """
    _keep_values = False ## keep the original values, only for debugging

    def __init__(self,value,datatag,Id,accept_errors_upto=.05):
        """
        :param value: values in string format
        :param dataTag: the dataTag (upperLimits or efficiencyMap)
        :param Id: an identifier, must be unique for each TxNameData!
        :param _accept_errors_upto: If None, do not allow extrapolations outside of
                convex hull.  If float value given, allow that much relative
                uncertainty on the upper limit / efficiency
                when extrapolating outside convex hull.
                This method can be used to loosen the equal branches assumption.
        """
        self.dataTag = datatag
        self._id = Id
        self._accept_errors_upto=accept_errors_upto
        self._V = None ## rotation matrix, derived from PCA
        self.loadData( value )
        if self._keep_values:
            self.value = value

    def __str__ ( self ):
        """ a simple unique string identifier, mostly for _memoize """
        return str ( self._id )

    def round_to_n ( self, x, n ):
        if x==0.0:
            return x
        return round(x, int( -np.sign(x)* int(floor(log10(abs(x)))) + (n - 1)))


    def __ne__ ( self, other ):
        return not self.__eq__ ( other )

    def __eq__ ( self, other ):
        if type(self) != type ( other ):
            return False
        return self._id == other._id

    def convertString ( self, value ):
        if not "GeV" in value:
            raise SModelSError("data string malformed: %s" % value)
        if "TeV" in value or "MeV" in value:
            raise SModelSError("data string malformed: %s" % value)
        s = value.replace ( "GeV", "" ).replace( "*", "" )
        if "fb" in value:
            self.unit = fb
            s = s.replace ( "fb", "" )
            return eval ( s )
        if "pb" in value:
            self.unit = pb
            s = s.replace ( "pb", "" )
            return eval ( s )
        self.unit = 1
        return eval ( s )

    def removeGeV ( self, branch ):
        if type ( branch ) == float:
            return branch
        ret = []
        for b in branch:
            els = []
            for element in b:
                if type(element)==unum.Unum:
                    els.append ( element.asNumber ( GeV ) )
                else:
                    els.append ( element )
            ret.append ( els )
        return ret
            
            # value = eval(value, {'fb':fb, 'pb':pb, 'GeV':GeV, 'TeV':TeV})
    def removeUnits ( self, value ):
        if type(value[0][1])==unum.Unum:
            ## if its a unum, we store 1.0 * unit
            self.unit=value[0][1] / ( value[0][1].asNumber() )
        ret = []
        for point in value:
            newpoint = []
            for branch in point:
                newbranch=branch
                if type (branch) == unum.Unum:
                    newbranch = ( branch / self.unit ).asNumber()
                else:
                    newbranch = self.removeGeV ( branch )
                newpoint.append ( newbranch )
            ret.append ( newpoint )
        return ret

    def loadData(self,value):
        """
        Uses the information in value to generate the data grid used for
        interpolation.
        """

        if self._V:
            return
        self.unit = 1.0 ## store the unit so that we can take arbitrary units for
                        ## the "z" values.  default is unitless,
                        ## which we use for efficiency maps

        if type(value) == str:
            value = self.convertString ( value )
        else:
            value = self.removeUnits ( value )

        if len(value) < 1 or len(value[0]) < 2:
                logger.error ( "input value not in correct format. expecting sth " \
                               "like [ [ [[ 300.*GeV,100.*GeV], "\
                               "[ 300.*GeV,100.*GeV] ], 10.*fb ], ... ] "\
                               "for upper limits or [ [ [[ 300.*GeV,100.*GeV],"\
                               " [ 300.*GeV,100.*GeV] ], .1 ], ... ] for "\
                               "efficiency maps. Received %s" % value[:80] )
        self.computeV( value )

    @_memoize
    def getValueFor(self,massarray):
        """
        Interpolates the value and returns the UL or efficiency for the
        respective massarray
        
        :param massarray: mass array values (with units), i.e.
                          [[100*GeV,10*GeV],[100*GeV,10*GeV]]
        """
        porig=self.flattenMassArray ( massarray ) ## flatten
        self.massarray = massarray ## only for bookkeeping and better error msgs
        if len(porig)!=self.full_dimensionality:
            logger.error ( "dimensional error. I have been asked to compare a "\
                    "%d-dimensional mass vector with %d-dimensional data!" % \
                    ( len(porig), self.full_dimensionality ) )
            return None
        p= ( (np.matrix(porig)[0] - self.delta_x ) ).tolist()[0]
        P=np.dot(p,self._V)  ## rotate
        dp = self.countNonZeros(P)
        self.projected_value = self.interpolate(P[:self.dimensionality])
        if dp > self.dimensionality: ## we have data in different dimensions
            if self._accept_errors_upto == None:
                return None
            logger.debug( "attempting to interpolate outside of convex hull "\
                    "(d=%d,dp=%d,masses=%s)" %
                     ( self.dimensionality, dp, str(massarray) ) )            
            return self._interpolateOutsideConvexHull( massarray )

        return self._returnProjectedValue()

    def flattenMassArray ( self, data ):
        """ flatten mass array and remove units """
        ret=[]
        for i in data:
            for j in i:
                if type(j) == unum.Unum:
                    ret.append ( j.asNumber(GeV) )
                else:
                    ret.append ( j )
        return ret

    def interpolate(self, point, fill_value=np.nan):
        
        tol = 1e-6

        # tol = sys.float_info.epsilon * 1e10
        simplex = self.tri.find_simplex(point, tol=tol)
        if simplex==-1: ## not inside any simplex?
            return fill_value
        
        #Transformation matrix for the simplex:
        simplexTrans = np.take(self.tri.transform, simplex, axis=0)
        #Space dimension:
        d = simplexTrans.shape[-1]
        #Rotation and translation to baryocentric coordinates:
        delta_x = simplexTrans[d,:]
        rot = simplexTrans[:d,:]
        bary = np.dot(rot,point-delta_x) #Point coordinates in the baryocentric system
        #Weights for the vertices:
        wts = np.append(bary, 1. - bary.sum())        
        #Vertex indices:        
        vertices = np.take(self.tri.simplices, simplex, axis=0)
        #Compute the value:
        values = np.array(self.xsecUnitless)
        ret = np.dot(np.take(values, vertices),wts)
        minXsec = min(np.take(values, vertices))
        if ret < minXsec:
            logger.debug('Interpolation below simplex values. Will take the smallest simplex value.')
            ret = minXsec
        return float(ret)


    def zeroIndices ( self ):
        """ return list of indices for vertices with zero y_values.
            dont consider vertices on the convex hull. """
        zeroes = set()
        for i,x in enumerate(self.y_values):
            if i in self.tri.convex_hull:
                continue
            if x < 1.e-9:
                zeroes.add(i)
        return zeroes

    def checkRemovableVertices ( self ):
        """ check if any of the vertices in the triangulation
            is removable, because all adjacent simplices are zero-only """
            
        t0=time.time()
        ## first get indices of zeroes not on the hull
        zeroes = self.zeroIndices() 
        if len(zeroes)<2: # a single zero cannot be removable
            return []
        removables = set()
        zeroSimplices = [] ## all zero-only simplices, by index
        verticesInSimplices = { x:[] for x in zeroes }
        for ctr,s in enumerate(self.tri.simplices):
            if self.checkZeroSimplex ( s, zeroes ):
                zeroSimplices.append ( ctr )
            for vtx in s: ## remember which vertex is in which simplex
                if not vtx in zeroes: ## only needed for zeroes though
                    continue
                verticesInSimplices[vtx].append ( ctr )

        for vtx in zeroes: ## for all zero vertices
            allSimplicesZero=True
            simplices = verticesInSimplices[vtx]
            for simplex in simplices: ## go through all simplces with our vtx
                if not simplex in zeroSimplices: ## not a zero simplex?
                    allSimplicesZero=False
                    break
            if allSimplicesZero:
                removables.add ( vtx )
        logger.debug( "checkRemovables spent %.3f s on %s simplices." \
                       "We had %d zeroes. Found %d removables." % \
                       ( time.time() - t0, ctr, len(zeroes), len(removables) ) )
        return removables

    def _estimateExtrapolationError(self, massarray):
        """ when projecting a point p from n to the point P in m dimensions, we
            estimate the expected extrapolation error with the following
            strategy: we compute the gradient at point P, and let alpha be the
            distance between p and P. We then walk one step of length alpha in
            the direction of the greatest ascent, and the opposite direction.
            Whichever relative change is greater is reported as the expected
            extrapolation error.
        """
        #p=self.flattenMassArray ( massarray ) ## point p in n dimensions
        porig=self.flattenMassArray ( massarray ) ## flatten
        p= ( (np.matrix(porig)[0] - self.delta_x ) ).tolist()[0]
        P=np.dot(p,self._V)                    ## projected point p in n dimensions
        ## P[self.dimensionality:] is project point p in m dimensions
        # m=self.countNonZeros ( P ) ## dimensionality of input
        ## how far are we away from the "plane": distance alpha
        alpha = float ( np.sqrt ( np.dot ( P[self.dimensionality:],
                        P[self.dimensionality:] ) ) )
        if alpha == 0.:
            ## no distance to the plane, so no extrapolation error
            return 0.
        ## the value of the grid at the point projected to the "plane"

        ## compute gradient
        gradient=[]
        for i in range ( self.dimensionality ):
            P2=copy.deepcopy(P)
            P2[i]+=alpha
            pv = self.interpolate( P2[:self.dimensionality] )
            g=float ( ( pv - self.projected_value ) / alpha )
            if math.isnan ( g ):
                ## if we cannot compute a gradient, we return nan
                return float("nan")
            gradient.append(g)
        ## normalize gradient
        C= float(np.sqrt( np.dot ( gradient, gradient ) ))
        if C == 0.:
            ## zero gradient? we return 0.
            return 0.
        for i,grad in enumerate(gradient):
            gradient[i]=grad/C*alpha
        ## walk one alpha along gradient
        P3=copy.deepcopy(P)
        P4=copy.deepcopy(P)
        for grad in gradient:
            P3[i]+= grad
            P4[i]-= grad
        agp=self.interpolate( P3[:self.dimensionality] )
        agm=self.interpolate( P4[:self.dimensionality] )
        dep,dem=0.,0.
        if self.projected_value == 0.:
            if agp!=0.:
                dep =1.0
            if agm!=0.:
                dem =1.0
        else:
            dep=abs ( agp - self.projected_value) / self.projected_value
            dem=abs ( agm - self.projected_value ) / self.projected_value
        de=dep
        if dem > de: de=dem
        return de

    def _interpolateOutsideConvexHull ( self, massarray ):
        """ experimental routine, meant to check if we can interpolate outside
            convex hull """
        de = self._estimateExtrapolationError(massarray)
        if de < self._accept_errors_upto:
            return self._returnProjectedValue()
        if not math.isnan(de):
            logger.debug ( "Expected propagation error of %f too large to " \
                           "propagate." % de )
        return None

    def _returnProjectedValue ( self ):
        ## None is returned without units'
        if self.projected_value is None or math.isnan(self.projected_value):
            logger.debug ( "projected value is None. Projected point not in " \
                    "convex hull? original point=%s" % self.massarray )
            return None
        #Set value to zero if it is lower than machine precision (avoids fake negative values)
        if abs(self.projected_value) < 100.*sys.float_info.epsilon:
            self.projected_value = 0.
        return self.projected_value * self.unit

    def countNonZeros ( self, mp ):
        """ count the nonzeros in a vector """
        nz=0
        for i in mp:
            if abs(i)>10**-4:
                nz+=1
        return nz

    def onlyZeroValues ( self ):
        """ check if the map is zeroes only """
        eps = sys.float_info.epsilon
        negative_values = bool ( sum ( [ x < -eps for x in self.xsecUnitless ] ) )
        if negative_values:
            for x in self.xsecUnitless:
                if x < -eps:
                    logger.error ( "negative error in result: %f, %s" % \
                                   ( x, self._id) )
                    sys.exit()
        if sum(self.xsecUnitless) > 0.:
            return False
        return True

    def computeV ( self, values ):
        """ compute rotation matrix _V, and triangulation self.tri """
        if self._V!=None:
            return
        Morig=[]
        xsec = np.ndarray ( shape = (len(values), ) )
        self.massdim = np.array(values[0][0]).shape

        for ctr,(x,y) in enumerate(values):
            xsec[ctr]=y
            xp = self.flattenMassArray(x)
            Morig.append( xp )
        self.xsecUnitless = [x.asNumber() if isinstance(x,unum.Unum) else float(x) 
                             for x in xsec]
        aM=np.matrix ( Morig )
        MT=aM.T.tolist()
        self.delta_x = np.matrix ( [ sum (x)/len(Morig) for x in MT ] )[0]
        M = []

        for Mx in Morig:
            m=(np.matrix(Mx) - self.delta_x).tolist()[0]
            M.append(m)

        try:
            ## we dont need thousands of points for SVD
            n = int(math.ceil ( len(M) / 2000. ) )
            Vt=svd(M[::n])[2]
        except Exception as e:
            logger.error ( "exception caught when performing singular value decomposition: %s, %s" % ( type(e), e ) )
            sys.exit()
        V=Vt.T
        self._V= V ## self.round ( V )
        Mp=[]

        ## the dimensionality of the whole mass space, disrespecting equal branches
        ## assumption
        self.full_dimensionality = len(xp)
        self.dimensionality=0
        for m in M:
            mp=np.dot(m,V)
            Mp.append ( mp )
            nz=self.countNonZeros(mp)
            if nz>self.dimensionality:
                self.dimensionality=nz
        MpCut=[]
        for i in Mp:
            MpCut.append(i[:self.dimensionality].tolist() )
        if self.dimensionality > 1:
            self.tri = qhull.Delaunay(MpCut)
        else:            
            self.tri = Delaunay1D(MpCut)           
        
    def _getMassArrayFrom(self,pt,unit=GeV):
        """
        Transforms the point pt in the PCA space to the original mass array
        :param pt: point with the dimentions of the data dimensionality (e.g. [x,y])
        :param unit: Unit for returning the mass array. If None, it will be
                     returned unitless
        :return: Mass array (e.g. [[mass1,mass2],[mass3,mass4]])
        """
        
        if self._V is None:
            logger.error("Data has not been loaded")
            return None
        if len(pt) != self.dimensionality:
            logger.error("Wrong point dimensions (%i), it should be %i" 
                         %(len(pt),self.dimensionality))
            return None
        fullpt = np.append(pt,[0.]*(self.full_dimensionality-len(pt)))
        mass = np.dot(self._V,fullpt) + self.delta_x
        mass = mass.reshape(self.massdim).tolist()
        if isinstance(unit,unum.Unum):
            mass = [[m*unit for m in br] for br in mass]

        return mass
        
    def hasNoZeroes(self):
        """
        Maybe we have no zeroes at all?
        """
        for i in self.y_values:
            if abs ( i ) < 1e-9:
                return False
        return True

    def removeExtraZeroes(self):        
        """
        Remove redundant zeroes in the triangulation
        """
        
        if self.hasNoZeroes():
            return ## no zeros? return original list
        
        removables = self.checkRemovableVertices() # check if we can remove vertices
        if len(removables) == 0:
            return
        logger.debug("We can remove %d points in %s!" % \
                       (len(removables), self._id ))
        newvalues = []
        for ctr,value in enumerate(self.value):
            if ctr not in removables:
                newvalues.append(value)
                
        self._V = None
        self.value = newvalues
        self.y_values = np.array(self.value)[:,1]        
        ##Recompute simplices
        self.computeV()
    
    def cleanUp(self):
        if self._keep_values:
            return
        if hasattr(self, "value"):
            del self.value
     
class Delaunay1D:
    """
    Uses a 1D data array to interpolate the data.
    The attribute simplices is a list of N-1 pair of ints with the indices of the points 
    forming the simplices (e.g. [[0,1],[1,2],[3,4],...]).    
    """
    
    def __init__(self,data):
        
        self.points = None
        self.simplices = None
        self.transform = None
        if data and self.checkData(data):            
            self.points = sorted(data)
            #Create simplices as the point intervals (using the sorted data)
            self.simplices = np.array([[data.index(self.points[i+1]),data.index(pt)] 
                                       for i,pt in enumerate(self.points[:-1])])
            transform = []
            #Create trivial transformation to the baryocentric coordinates:
            for simplex in self.simplices:
                xmax,xmin = data[simplex[0]][0],data[simplex[1]][0]
                transform.append([[1./(xmax-xmin)],[xmin]])
            self.transform = np.array(transform)
            
            #Store convex hull (first and last point):
            self.convex_hull = np.array([data.index(self.points[0]),data.index(self.points[-1])])
            
        else:
            raise SModelSError()
        
    def find_simplex(self,x,tol=0.):
        """
        Find 1D data interval (simplex) to which x belongs
        
        :param x: Point (float) without units
        :param tol: Tolerance. If x is outside the data range with distance < tol, extrapolate.
        
        :return: simplex index (int)
        """
        
        xi = self.find_index(self.points,x)
        if xi == -1:
            if abs(x-self.points[0]) < tol:
                return 0
            else:
                return -1
        elif xi == len(self.simplices):
            if abs(x-self.points[-1]) < tol:
                return xi-1
            else:
                return -1
        else:
            return xi    
    
    def checkData(self,data):
        """
        Define the simplices according to data. Compute and store
        the transformation matrix and simplices self.point.
        """
        if not isinstance(data,list):
            logger.error("Input data for 1D Delaunay should be a list.")
            return False
        for pt in data:
            if (not isinstance(pt,list)) or len(pt) != 1 or (not isinstance(pt[0],float)):
                logger.error("Input data for 1D Delaunay is in wrong format. It should be [[x1],[x2],..]")
                return False
        return True
    
    
    def find_index(self,xlist, x):
        """
        Efficient way to find x in a list.
        Returns the index (i) of xlist such that xlist[i] < x <= xlist[i+1].
        If x > max(xlist), returns the length of the list.
        If x < min(xlist), returns 0.        vertices = np.take(self.tri.simplices, simplex, axis=0)
        temp = np.take(self.tri.transform, simplex, axis=0)
        d=temp.shape[2]
        delta = uvw - temp[:, d]


        :param xlist: List of x-type objects
        :param x: object to be searched for.

        :return: Index of the list such that xlist[i] < x <= xlist[i+1].
        """

        lo = 0    
        hi = len(xlist)
        while lo < hi:
            mid = (lo+hi)//2
            if xlist[mid] < x: lo = mid+1
            else: hi = mid
        return lo-1     


if __name__ == "__main__":
    import time
    data = [ [ [[ 150.*GeV, 50.*GeV], [ 150.*GeV, 50.*GeV] ],  3.*fb ],
         [ [[ 200.*GeV,100.*GeV], [ 200.*GeV,100.*GeV] ],  5.*fb ],
         [ [[ 300.*GeV,100.*GeV], [ 300.*GeV,100.*GeV] ], 10.*fb ],
         [ [[ 300.*GeV,150.*GeV], [ 300.*GeV,150.*GeV] ], 13.*fb ],
         [ [[ 300.*GeV,200.*GeV], [ 300.*GeV,200.*GeV] ], 15.*fb ],
         [ [[ 300.*GeV,250.*GeV], [ 300.*GeV,250.*GeV] ], 20.*fb ],
         [ [[ 400.*GeV,100.*GeV], [ 400.*GeV,100.*GeV] ],  8.*fb ],
         [ [[ 400.*GeV,150.*GeV], [ 400.*GeV,150.*GeV] ], 10.*fb ],
         [ [[ 400.*GeV,200.*GeV], [ 400.*GeV,200.*GeV] ], 12.*fb ],
         [ [[ 400.*GeV,250.*GeV], [ 400.*GeV,250.*GeV] ], 15.*fb ],
         [ [[ 400.*GeV,300.*GeV], [ 400.*GeV,300.*GeV] ], 17.*fb ],
         [ [[ 400.*GeV,350.*GeV], [ 400.*GeV,350.*GeV] ], 19.*fb ], ]
    txnameData=TxNameData ( data, "upperLimits",  sys._getframe().f_code.co_name )
    t0=time.time()
    for masses in [ [[ 302.*GeV,123.*GeV], [ 302.*GeV,123.*GeV]],
                    [[ 254.*GeV,171.*GeV], [ 254.*GeV,170.*GeV]],
    ]:
        result=txnameData.getValueFor( masses )
        sm = "%.1f %.1f" % ( masses[0][0].asNumber(GeV), masses[0][1].asNumber(GeV) )
        print ( "%s %.3f fb" % ( sm, result.asNumber(fb) ) )
    print ( "%.2f ms" % ( (time.time()-t0)*1000. ) )
