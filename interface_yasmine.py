import sys
import cv2

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)


class InterfaceOperateur(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface opérateur")
        self.resize(1000, 700)

        # -----------------------------
        # Variables simples
        # -----------------------------
        self.nom_operateur = "NOM OPERATEUR"
        self.mode_manuel = False
        self.mode_urgence = False
        self.etat_tapis = False
        self.sens_tapis = "STOP"   # LEFT / RIGHT / STOP
        self.etape_demo = 0
        self.flash_urgence = False

        # -----------------------------
        # Widget principal
        # -----------------------------
        self.zone_principale = QWidget()
        self.setCentralWidget(self.zone_principale)
        self.zone_principale.setStyleSheet("background-color: lightgray;")

        self.layout_principal = QVBoxLayout()
        self.zone_principale.setLayout(self.layout_principal)

        # -----------------------------
        # Nom opérateur
        # -----------------------------
        self.label_operateur = QLabel(self.nom_operateur)
        self.label_operateur.setAlignment(Qt.AlignCenter)
        self.label_operateur.setStyleSheet("font-size: 28px; font-weight: bold;")
        self.layout_principal.addWidget(self.label_operateur)

        # -----------------------------
        # Partie haute
        # -----------------------------
        self.layout_haut = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_haut)

        # Colonne gauche
        self.layout_gauche = QVBoxLayout()
        self.layout_haut.addLayout(self.layout_gauche, 1)

        self.label_manuel_titre = QLabel("MODE MANUEL")
        self.label_manuel_titre.setAlignment(Qt.AlignCenter)
        self.label_manuel = QLabel("OFF")
        self.label_manuel.setAlignment(Qt.AlignCenter)
        self.label_manuel.setFixedHeight(60)

        self.label_urgence_titre = QLabel("MODE URGENCE")
        self.label_urgence_titre.setAlignment(Qt.AlignCenter)
        self.label_urgence = QLabel("OFF")
        self.label_urgence.setAlignment(Qt.AlignCenter)
        self.label_urgence.setFixedHeight(60)

        self.layout_gauche.addWidget(self.label_manuel_titre)
        self.layout_gauche.addWidget(self.label_manuel)
        self.layout_gauche.addSpacing(30)
        self.layout_gauche.addWidget(self.label_urgence_titre)
        self.layout_gauche.addWidget(self.label_urgence)
        self.layout_gauche.addStretch()

        # Colonne droite = caméra
        self.layout_droite = QVBoxLayout()
        self.layout_haut.addLayout(self.layout_droite, 2)

        self.label_camera = QLabel("CAMERA")
        self.label_camera.setAlignment(Qt.AlignCenter)
        self.label_camera.setMinimumSize(640, 360)
        self.label_camera.setStyleSheet(
            "background-color: white; border: 3px solid black; font-size: 30px;"
        )
        self.layout_droite.addWidget(self.label_camera)

        self.label_alerte = QLabel("ARRET D'URGENCE")
        self.label_alerte.setAlignment(Qt.AlignCenter)
        self.label_alerte.setStyleSheet(
            "background-color: darkred; color: white; font-size: 24px; font-weight: bold; padding: 8px;"
        )
        self.label_alerte.hide()
        self.layout_droite.addWidget(self.label_alerte)

        # -----------------------------
        # Partie basse = tapis
        # -----------------------------
        self.layout_bas = QVBoxLayout()
        self.layout_principal.addLayout(self.layout_bas)

        self.layout_fleches = QHBoxLayout()
        self.layout_bas.addLayout(self.layout_fleches)

        self.fleche_gauche = QLabel("←")
        self.fleche_gauche.setAlignment(Qt.AlignCenter)
        self.fleche_gauche.setStyleSheet("font-size: 120px; color: gray;")

        self.fleche_droite = QLabel("→")
        self.fleche_droite.setAlignment(Qt.AlignCenter)
        self.fleche_droite.setStyleSheet("font-size: 120px; color: gray;")

        self.layout_fleches.addStretch()
        self.layout_fleches.addWidget(self.fleche_gauche)
        self.layout_fleches.addWidget(self.fleche_droite)
        self.layout_fleches.addStretch()

        self.label_tapis_titre = QLabel("ETAT TAPIS")
        self.label_tapis_titre.setAlignment(Qt.AlignCenter)
        self.label_tapis = QLabel("OFF")
        self.label_tapis.setAlignment(Qt.AlignCenter)
        self.label_tapis.setFixedHeight(60)

        self.layout_bas.addWidget(self.label_tapis_titre)
        self.layout_bas.addWidget(self.label_tapis)

        # -----------------------------
        # Camera très simple
        # -----------------------------
        self.camera_index = 0
        self.capture = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        self.timer_camera = QTimer()
        self.timer_camera.timeout.connect(self.lire_camera)

        # -----------------------------
        # Demo très simple
        # -----------------------------
        self.timer_demo = QTimer()
        self.timer_demo.timeout.connect(self.changer_demo)

        self.timer_flash = QTimer()
        self.timer_flash.timeout.connect(self.clignoter_urgence)

        self.mettre_a_jour_interface()

    def demarrer(self):
        self.timer_camera.start(30)
        self.timer_demo.start(2000)

    def lire_camera(self):
        if not self.capture.isOpened():
            self.label_camera.setText("Camera non trouvee")
            return

        ok, image = self.capture.read()

        if not ok:
            self.label_camera.setText("Erreur camera")
            return

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w, c = image.shape
        image_qt = QImage(image.data, w, h, c * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image_qt)

        pixmap = pixmap.scaled(
            self.label_camera.width(),
            self.label_camera.height(),
            Qt.KeepAspectRatio,
        )

        self.label_camera.setPixmap(pixmap)
        self.label_camera.setText("")

    def mettre_a_jour_interface(self):
        self.label_operateur.setText(self.nom_operateur)

        if self.mode_manuel:
            self.label_manuel.setText("ON")
            self.label_manuel.setStyleSheet(
                "background-color: green; color: white; font-size: 24px; font-weight: bold;"
            )
        else:
            self.label_manuel.setText("OFF")
            self.label_manuel.setStyleSheet(
                "background-color: red; color: white; font-size: 24px; font-weight: bold;"
            )

        if self.mode_urgence:
            self.label_urgence.setText("ON")
            self.label_urgence.setStyleSheet(
                "background-color: red; color: white; font-size: 24px; font-weight: bold;"
            )
            self.label_alerte.show()
            if not self.timer_flash.isActive():
                self.timer_flash.start(300)
        else:
            self.label_urgence.setText("OFF")
            self.label_urgence.setStyleSheet(
                "background-color: green; color: white; font-size: 24px; font-weight: bold;"
            )
            self.label_alerte.hide()
            self.timer_flash.stop()
            self.label_camera.setStyleSheet(
                "background-color: white; border: 3px solid black; font-size: 30px;"
            )

        if self.etat_tapis:
            self.label_tapis.setText("ON")
            self.label_tapis.setStyleSheet(
                "background-color: green; color: white; font-size: 24px; font-weight: bold;"
            )
        else:
            self.label_tapis.setText("OFF")
            self.label_tapis.setStyleSheet(
                "background-color: red; color: white; font-size: 24px; font-weight: bold;"
            )

        if self.mode_urgence:
            self.fleche_gauche.setStyleSheet("font-size: 120px; color: red;")
            self.fleche_droite.setStyleSheet("font-size: 120px; color: red;")
        else:
            if self.sens_tapis == "LEFT":
                self.fleche_gauche.setStyleSheet("font-size: 120px; color: green;")
                self.fleche_droite.setStyleSheet("font-size: 120px; color: gray;")
            elif self.sens_tapis == "RIGHT":
                self.fleche_gauche.setStyleSheet("font-size: 120px; color: gray;")
                self.fleche_droite.setStyleSheet("font-size: 120px; color: green;")
            else:
                self.fleche_gauche.setStyleSheet("font-size: 120px; color: gray;")
                self.fleche_droite.setStyleSheet("font-size: 120px; color: gray;")

    def clignoter_urgence(self):
        self.flash_urgence = not self.flash_urgence

        if self.flash_urgence:
            self.label_camera.setStyleSheet(
                "background-color: white; border: 6px solid red; font-size: 30px;"
            )
            self.label_alerte.setStyleSheet(
                "background-color: red; color: white; font-size: 24px; font-weight: bold; padding: 8px;"
            )
        else:
            self.label_camera.setStyleSheet(
                "background-color: white; border: 6px solid darkred; font-size: 30px;"
            )
            self.label_alerte.setStyleSheet(
                "background-color: darkred; color: white; font-size: 24px; font-weight: bold; padding: 8px;"
            )

    def changer_demo(self):
        self.etape_demo = self.etape_demo + 1
        numero = self.etape_demo % 6

        if numero == 0:
            self.nom_operateur = "NOM OPERATEUR"
            self.mode_manuel = False
            self.mode_urgence = False
            self.etat_tapis = False
            self.sens_tapis = "STOP"

        elif numero == 1:
            self.nom_operateur = "YASMINE"
            self.mode_manuel = True
            self.mode_urgence = False
            self.etat_tapis = False
            self.sens_tapis = "STOP"

        elif numero == 2:
            self.nom_operateur = "YASMINE"
            self.mode_manuel = True
            self.mode_urgence = False
            self.etat_tapis = True
            self.sens_tapis = "LEFT"

        elif numero == 3:
            self.nom_operateur = "YASMINE"
            self.mode_manuel = True
            self.mode_urgence = False
            self.etat_tapis = True
            self.sens_tapis = "RIGHT"

        elif numero == 4:
            self.nom_operateur = "YASMINE"
            self.mode_manuel = False
            self.mode_urgence = True
            self.etat_tapis = False
            self.sens_tapis = "STOP"

        elif numero == 5:
            self.nom_operateur = "YASMINE"
            self.mode_manuel = False
            self.mode_urgence = False
            self.etat_tapis = False
            self.sens_tapis = "STOP"

        self.mettre_a_jour_interface()

    def closeEvent(self, event):
        self.timer_camera.stop()
        self.timer_demo.stop()
        self.timer_flash.stop()

        if self.capture.isOpened():
            self.capture.release()

        event.accept()


def main():
    app = QApplication(sys.argv)
    fenetre = InterfaceOperateur()
    fenetre.show()
    fenetre.demarrer()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
