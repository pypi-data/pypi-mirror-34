"""Base Datapoint Types

``DataPointType`` Metaclass
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: nc5ng.types.DataPointType
  :members:

"""

import logging



class DataPointType(type):
    """ Metaclass for DataPoints, defines class creation and class/hierarchy member variables 
    
    The meta-class in part, hides some of the more rote requirements of our datapoint type
    from the actual object hierarchy

    This allows some magic like run-time casting to the correct datapoint without knowing the 
    type specifically, and a persisitent library-wide memory backed database for quick retrieval and to minimize replication

    To understand the meta class, there are a number of tutorials available online, roughly speaking this class is what is used to "create" the DataPoint class, and allows us to manipulate the class without needing any implementation details. 


    Defining a new DataPointType Hierarchy simply requires using this class as the metaclass

        class NewDataPoint(metaclass=DataPointType):
          pass

    By creating a new DataPointType, the following changes will be done to the final class

      - The type will have a database (dictionary) of types registered with the base class
      - Each type and subtype will have a point container (default set) created
      - The shorthand name will be generated from the class name
      - Instance Creation will be overidden and allow creation of any other data type by specifting the type shorthand as an argument
      

    Class Configuration:

    Each new type has some meta-configuration available

    1. To override data point registration 
       - Create a `@classmethod`  `__register__(cls, point)` to overide how a new point is registered/saved
       - Create a class member `_point_store` to change the underlying storage type (from set)
    2. Override shorthand name by specific '_type_shorthand' explicitly in the class
    
    
    Any class that uses this type as a metaclass will be registered 
    """
    @classmethod
    def __prepare__(metacls, name, bases, **kargs):
        """ Prepare the new class, here for completeness
        """
        logging.debug("Preparing Class %s"%name)
        return super().__prepare__(name, bases, **kargs)


    @property
    def type_shorthand(cls):
        """ Get the class shorthand name"""
        return cls._type_shorthand
    
    @property
    def point_store(cls):
        """ Return the type-specific Point Buffer"""
        return cls._point_store

    @property
    def point_database(cls):
        """ Return the Root Database of all DataPoints in this Hierarchy"""
        return cls._cbdb
    
    
    def __new__(metacls, name, bases, namespace,  **kargs):
        """ Create a new data point type, called on class load

        Creates class attributes level point set for storage
        
        metaclass __new__ is executed on load time for every
        class that uses it, it is executed after __prepare__ which
        constructs the class object
        """

    
        logging.debug("Creating Class %s"%name)
        cls = super().__new__(metacls, name, bases, namespace)
        
        if not(hasattr(cls, '_cbdb')):
            logging.debug("Creating Data Point Database")
            cls._cbdb = dict()


        # Shorthand Name
        cls._type_shorthand =  name.lower()
        while cls._type_shorthand in cls._cbdb:
            cls._type_shorthand = cls._type_shorthand + "_" # in case of name conflict, add underscore

        # Point Storage
        cls._point_store = namespace.get('_point_store', set() )
        
        
        logging.debug("Registering new Data Point Type %s with shorthand %s"%(name, cls._type_shorthand))

        
        cls._cbdb[cls.type_shorthand]={'type':cls, 'points': cls._point_store }
        return cls

    
    def __init__(cls, name, bases, namespace):
        """ Initialize a new FileBacked Class

        This is a slot method for class creation, __init__ is called when class is defined (load time)

        \param cls - reference to new type, similiar to @classmethod
        \param name - new class name
        \param bases - base classes
        \param namespace - new class attributes
        \param Parser - BaseFileParser underlying this type
        \param **kwargs - keywords passed to Parser initialization
        
        """        
        logging.debug("Creating Data Point Class %s"%name)

        super().__init__(name, bases, namespace)


    def __register__(cls, point):
        """ Register a point with the class buffer """
        cls._point_store.add(point)

    def __call__(cls, *args,  **kw):
        """ Create a new Point in this hierarchy"""

        """
        if typename is not None:
            if typename not in cls._cbdb:
                raise TypeError("Invalid Data Point Type with Shorthand %s"%typename)
            cls = cls._cbdb[typename]['type']
        """
        if args and (args[0] in cls.point_database.keys()):
            typename=args[0]
        elif kw and ('type' in kw):
            typename = kw['type']
        else:
            typename = cls.type_shorthand


        if typename == cls.type_shorthand:
            point = super().__call__(*args, **kw)
            if not getattr(point, 'ephemeral', False):
                cls.__register__(point)
        elif typename in cls.point_database.keys():
            point = cls.point_database[typename]['type'].__call__(*args, **kw)
        else:
            return None

        return point

    
