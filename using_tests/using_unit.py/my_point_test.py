# we can use the built in unittest
import unittest 

from my_point_class import Point # import the thing to be tested

class testPoint(unittest.TestCase): # inherit from TestCase
    # set up before each test is run
    def setUp(self):
        # this code will run before each test 
        self.point = Point(3,5) # we make sure each test is independent
    # here are the tests

    def testPointCounter(self):
        ''' test that we can accurately count the number of point instances'''
        self.assertGreater(Point.points, 1) # at least one point!!

    def testMoveBy_a(self):
        '''Test the moveBy method with altered x and y values'''
        self.point.moveBy(5,2) # (8,7)
        # make an asertion
        self.assertEqual( self.point.display(), (8,7) )

    def testMoveBy_b(self):
        '''Test the moveBy method with negative x and y values'''
        self.point.moveBy(-5,-2) # (-2, 3)
        # make an asertion
        self.assertEqual( self.point.display(), (-2, 3) )
    
    def testMoveBy_c(self):
        '''Test the moveBy method with default dx value'''
        self.point.moveBy(dy=9) # use the default dx
        # make an asertion
        self.assertEqual( self.point.display(), (3, 14) )

    def testHypot_a(self):
        ''' derive the hypotenuse from the x and y values'''
        self.point.moveBy(0, -1) # (3, 4)
        r = self.point.hypot()
        self.assertEqual(r, 5.00)

    def testHypot_b(self):
        ''' derive the hypotenuse for difficult x and y values'''
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.83, places=2) # works!!
    
    def testHypot_c(self):
        ''' derive the hypotenuse for -ve x and y values'''
        self.pos = Point(3,4)
        self.neg = Point(-3, -4)
        self.assertEqual(self.pos.hypot(), self.neg.hypot()) 

    def testExceptionRaised(self):
        '''if x or y are non ineger we expect a TypeError'''
        with self.assertRaises(TypeError):
            Point('3', 4) # string where we expect an int

    def testAlmost(self): # here we verify rounding is mathematically correct
        m = 5.83
        n = 5.84
        j = 5.832 
        k = 5.835 
        l = 5.837 # 5.84
        self.assertAlmostEqual(m, j, places=2)
        self.assertAlmostEqual(n, k, places=2)
        self.assertAlmostEqual(n, l, places=2)

if __name__ == '__main__':
    unittest.main() # this invokes our tests