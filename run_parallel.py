import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

# Lista de archivos de features
FEATURES = [
    "features/login.feature",
    "features/search.feature",
    # agrega más si los tienes
]
SCENARIOS=[
    "@validacion_login_incorrecto",
    "@validacion_login_correcto"
]

def run_tests(tests):
    # Creamos el comando para Behave con Allure y Selenium Grid
    command = [
        "behave",
        "-f", "allure_behave.formatter:AllureFormatter",
        "-o", f"allure-files",
        "--tags",tests
    ]
    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tests, result.returncode, result.stdout.decode(), result.stderr.decode()

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(run_tests, SCENARIOS)

    for file, code, out, err in results:
        print(f"\n=== Resultado para {file} ===")
        print(f"Return Code: {code}")
        print(out)
        if code != 0:
            print("⚠️ Error:")
            print(err)