import os
import unittest

from main import *

def getDirectory(rel_dir):
    script_dir = os.path.dirname(__file__)
    complete_dir = script_dir + rel_dir
    return complete_dir

errado_1 = getDirectory("/audio/errado_1.wav")
errado_2 = getDirectory("/audio/errado_2.wav")

habitat_chita = getDirectory("/audio/habitat_chita.wav")
familia_chita = getDirectory("/audio/familia_chita.wav")
pais_chita = getDirectory("/audio/pais_chita.wav")
habitat_leao = getDirectory("/audio/habitat_leao.wav")
familia_leao = getDirectory("/audio/familia_leao.wav")
pais_leao = getDirectory("/audio/pais_leao.wav")
habitat_periquito = getDirectory("/audio/habitat_periquito.wav")
familia_periquito = getDirectory("/audio/familia_periquito.wav")
pais_periquito = getDirectory("/audio/pais_periquito.wav")
habitat_salamandra = getDirectory("/audio/habitat_salamandra.wav")
familia_salamandra = getDirectory("/audio/familia_salamandra.wav")
pais_salamandra = getDirectory("/audio/pais_salamandra.wav")
habitat_cachorro = getDirectory("/audio/habitat_cachorro.wav")
familia_cachorro = getDirectory("/audio/familia_cachorro.wav")
pais_cachorro = getDirectory("/audio/pais_cachorro.wav")
habitat_pato = getDirectory("/audio/habitat_pato.wav")
familia_pato = getDirectory("/audio/familia_pato.wav")
pais_pato = getDirectory("/audio/pais_pato.wav")

# agendar_1 = getDirectory("/audio/agendar_1.wav")
# cortes_1 = getDirectory("/audio/cortes_1.wav")
# disponibilidade_1 = getDirectory("/audio/disponibilidade_1.wav")
# fila_1 = getDirectory("/audio/fila_1.wav")
# horario_1 = getDirectory("/audio/horario_1.wav")
# agamento_1 = getDirectory("/audio/pagamento_1.wav")
# produtos_1 = getDirectory("/audio/produtos_1.wav")
# saudacao_1 = getDirectory("/audio/saudacao_1.wav")
        
class TesteNome(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_sem_nome(self):
        phrase = hear_audio(errado_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "")

    def testar_nome_errado(self):
        phrase = hear_audio(errado_2)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "")

class TesteLeao(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_familia(self):
        phrase_familia = hear_audio(familia_leao)
        print(f"comando reconhecido: {phrase_familia}")

        action, target = get_tokenized_command(phrase_familia)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva a família do leão")

    def testar_pais(self):
        phrase_pais = hear_audio(pais_leao)
        print(f"comando reconhecido: {phrase_pais}")

        action, target = get_tokenized_command(phrase_pais)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o país de origem do leão?")

    def testar_habitat(self):
        phrase_habitat = hear_audio(habitat_leao)
        print(f"comando reconhecido: {phrase_habitat}")

        action, target = get_tokenized_command(phrase_habitat)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o habitat natural do leão?")

class TesteChita(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_familia(self):
        phrase_familia = hear_audio(familia_chita)
        print(f"comando reconhecido: {phrase_familia}")

        action, target = get_tokenized_command(phrase_familia)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva a família da chita")

    def testar_pais(self):
        phrase_pais = hear_audio(pais_chita)
        print(f"comando reconhecido: {phrase_pais}")

        action, target = get_tokenized_command(phrase_pais)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o país de origem da chita?")

    def testar_habitat(self):
        phrase_habitat = hear_audio(habitat_chita)
        print(f"comando reconhecido: {phrase_habitat}")

        action, target = get_tokenized_command(phrase_habitat)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o habitat natural da chita?")

class TesteSalamandra(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_familia(self):
        phrase_familia = hear_audio(familia_salamandra)
        print(f"comando reconhecido: {phrase_familia}")

        action, target = get_tokenized_command(phrase_familia)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva a família da salamandra")

    def testar_pais(self):
        phrase_pais = hear_audio(pais_salamandra)
        print(f"comando reconhecido: {phrase_pais}")

        action, target = get_tokenized_command(phrase_pais)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o país de origem da salamandra?")

    def testar_habitat(self):
        phrase_habitat = hear_audio(habitat_salamandra)
        print(f"comando reconhecido: {phrase_habitat}")

        action, target = get_tokenized_command(phrase_habitat)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o habitat natural da salamandra?")

class TesteCachorro(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_familia(self):
        phrase_familia = hear_audio(familia_cachorro)
        print(f"comando reconhecido: {phrase_familia}")

        action, target = get_tokenized_command(phrase_familia)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva a família do cachorro")

    def testar_pais(self):
        phrase_pais = hear_audio(pais_cachorro)
        print(f"comando reconhecido: {phrase_pais}")

        action, target = get_tokenized_command(phrase_pais)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva o país de origem do cachorro")

    def testar_habitat(self):
        phrase_habitat = hear_audio(habitat_cachorro)
        print(f"comando reconhecido: {phrase_habitat}")

        action, target = get_tokenized_command(phrase_habitat)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o habitat natural do cachorro?")

class TestePato(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_familia(self):
        phrase_familia = hear_audio(familia_pato)
        print(f"comando reconhecido: {phrase_familia}")

        action, target = get_tokenized_command(phrase_familia)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva a família do pato")

    def testar_pais(self):
        phrase_pais = hear_audio(pais_pato)
        print(f"comando reconhecido: {phrase_pais}")

        action, target = get_tokenized_command(phrase_pais)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o país de origem do pato?")

    def testar_habitat(self):
        phrase_habitat = hear_audio(habitat_pato)
        print(f"comando reconhecido: {phrase_habitat}")

        action, target = get_tokenized_command(phrase_habitat)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o habitat natural do pato?")

class TestePeriquito(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_familia(self):
        phrase_familia = hear_audio(familia_periquito)
        print(f"comando reconhecido: {phrase_familia}")

        action, target = get_tokenized_command(phrase_familia)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "no contexto da biologia, descreva a família do periquito")

    def testar_pais(self):
        phrase_pais = hear_audio(pais_periquito)
        print(f"comando reconhecido: {phrase_pais}")

        action, target = get_tokenized_command(phrase_pais)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o país de origem do periquito?")

    def testar_habitat(self):
        phrase_habitat = hear_audio(habitat_periquito)
        print(f"comando reconhecido: {phrase_habitat}")

        action, target = get_tokenized_command(phrase_habitat)
        is_valid,response = run_command_two(action, target)

        self.assertTrue(response == "Qual o habitat natural do periquito?")


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    # testes.addTest(carregador.loadTestsFromTestCase(TesteNome))
    testes.addTest(carregador.loadTestsFromTestCase(TesteLeao))
    testes.addTest(carregador.loadTestsFromTestCase(TesteChita))
    testes.addTest(carregador.loadTestsFromTestCase(TesteSalamandra))
    testes.addTest(carregador.loadTestsFromTestCase(TesteCachorro))
    testes.addTest(carregador.loadTestsFromTestCase(TestePato))
    testes.addTest(carregador.loadTestsFromTestCase(TestePeriquito))

    executor = unittest.TextTestRunner()
    executor.run(testes)