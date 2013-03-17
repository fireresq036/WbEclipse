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
        self.service_part = None
        self.qualifier_part = None

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
        if len(elements) > 4:
            raise EclipseException("too many elements")
        if len(elements) < 3:
            raise EclipseException("too few elements")
        self.major_part = str(elements[0])
        self.minor_part = str(elements[1])
        if (len(elements) > 2):
            self.service_part = str(elements[2])
        if (len(elements) > 3):
            self.qualifier_part = str(elements[3])

    def major(self):
        return self.major_part

    def minor(self):
        return self.minor_part

    def service(self):
        if self.service_part is None:
            raise EclipseException("no service was specified")
        return self.service_part

    def qualifier(self):
        if self.qualifier_part is None:
            raise EclipseException("no qualifier was specified")
        return self.qualifier_part

    def qualifierWithoutDots(self):
        return '{0}{1}{2}{3}'.format(self.major_part, self.minor_part,
                                     self.service(), self.qualifier())

    def qualifierWithDots(self):
        return '{0}.{1}.{2}.{3}'.format(self.major_part, self.minor_part,
                                        self.service(), self.qualifier())

    def fullWithoutDots(self):
        return '{0}{1}{2}'.format(self.major_part, self.minor_part,
                                        self.service())

    def fullWithDots(self):
        return '{0}.{1}.{2}'.format(self.major_part, self.minor_part,
                                        self.service())

    def shortWintoutDots(self):
        return '{0}{1}'.format(self.major_part, self.minor_part)

    def shortWithDots(self):
        return '{0}.{1}'.format(self.major_part, self.minor_part)

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
