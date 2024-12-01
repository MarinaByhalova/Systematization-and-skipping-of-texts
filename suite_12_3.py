import unittest
import tests_12_3

object1 = unittest.TestSuite()
object1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
object1.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
object2 = unittest.TextTestRunner(verbosity=2)
object2.run(object1)