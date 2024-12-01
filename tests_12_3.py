import unittest

class Runner:

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = Runner(name='ran1')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Runner(name='ran2')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner(name='ran1')
        runner_2 = Runner(name='run2')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        self.all_results = {}
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner(name='Усэйн', speed=10)
        self.runner2 = Runner(name='Андрей', speed=9)
        self.runner3 = Runner(name='Ник', speed=3)
        self.distan = 90

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        tourne_1 = Tournament(self.distan, self.runner1, self.runner3)
        result = tourne_1.start()
        self.all_results['test_tourne1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        tourne_2 = Tournament(self.distan, self.runner2, self.runner3)
        result = tourne_2.start()
        self.all_results['test_tourne2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        tourne_3 = Tournament(self.distan, self.runner1, self.runner2, self.runner3)
        result = tourne_3.start()
        self.all_results['test_tourne3'] = result
if __name__ == '__main__':
    unittest.main()