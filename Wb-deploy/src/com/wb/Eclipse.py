'''
Created on Feb 7, 2013

@author: mrrussell
'''

class EclipseException(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(EclipseException).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

class Eclipse(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Create and instance of an Eclpse
        '''
        self.major_part = None
        self.minor_part = None
        self.patch_part = None

    def parseVersion(self, version):
        to_parse = str(version)
        data = ""
        elements = []
        for element in to_parse:
            if (element == '.'):
                if (len(data) == 0):
                    raise EclipseException("could not parse %s" %
                                           to_parse)
                elements.append(data)
                data = ""
            else:
                data += element
        if (len(data) > 0):
            elements.append(data)
        if len(elements) > 3:
            raise EclipseException("too many elements")
        if len(elements) == 0:
            raise EclipseException("too few elements")
        self.major_part = str(elements[0])
        self.minor_part = str(elements[1])
        if (len(elements) > 2):
            self.patch_part = str(elements[2])

    def major(self):
        return self.major_part

    def minor(self):
        return self.minor_part

    def patch(self):
        if self.patch_part is None:
            raise EclipseException("no patch was specified")
        return self.patch_part

    def fullWithoutDots(self):
        return "%s%s%s" % (self.major_part, self.minor_part, self.patch_part)

    def fullWithDots(self):
        return "%s.%s.%s" % (self.major_part, self.minor_part, self.patch_part)

    def shortWintoutDots(self):
        return "%s%s" % (self.major_part, self.minor_part)

    def shortWithDots(self):
        return "%s.%s" % (self.major_part, self.minor_part)

    def displayFull(self):
        print self.fullWithDots()

    def displayShort(self):
        print self.shortWithDots()


ECLIPSE_350 = Eclipse()
ECLIPSE_350.parseVersion("3.5.0")
ECLIPSE_360 = Eclipse()
ECLIPSE_360.parseVersion("3.6.0")
ECLIPSE_370 = Eclipse()
ECLIPSE_370.parseVersion("3.7.0")
ECLIPSE_380 = Eclipse()
ECLIPSE_380.parseVersion("3.8.0")
ECLIPSE_420 = Eclipse()
ECLIPSE_420.parseVersion("4.2.0")
ECLIPSE_430 = Eclipse()
ECLIPSE_430.parseVersion("4.3.0")
