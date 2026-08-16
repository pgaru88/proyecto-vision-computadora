
from deepface import DeepFace

def verificar_acceso(foto_registro, foto_intento):
    print("\n🔍 Analizando rostros...")

    try:
        resultado = DeepFace.verify(
            img1_path=foto_registro,
            img2_path=foto_intento,
            detector_backend="mtcnn"
        )

        print("\n==============================")

        if resultado["verified"]:
            print("✅ ACCESO PERMITIDO")
            print("El rostro coincide con la persona registrada.")
        else:
            print("❌ ACCESO DENEGADO")
            print("El rostro NO coincide con la persona registrada.")

        print("==============================")

    except Exception as error:
        print("⚠️ No fue posible realizar la verificación.")
        print("Error:", error)


print("============================================")
print(" SISTEMA DE INICIO DE SESIÓN CON DEEPFACE")
print("============================================")

foto_registro = input("\nEscribe la ruta de la foto registrada: ")
foto_intento = input("Escribe la ruta de la foto para iniciar sesión: ")

verificar_acceso(foto_registro, foto_intento)
