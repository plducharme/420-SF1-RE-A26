from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QLabel, QMainWindow, QWidget, QVBoxLayout, QTextEdit
from PySide6.QtGui import QPixmap

from roche_papier_ciseaux import partie_rpc


class JeuRochePapierCiseaux(QMainWindow):

    def __init__(self):
        super().__init__()

        self.disposition = QGridLayout()
        self.widget_central = QWidget()
        self.widget_central.setLayout(self.disposition)
        self.setCentralWidget(self.widget_central)

        self.disposition_joueur = QVBoxLayout()

        grandeur_bouton = QSize(200, 100)
        self.bouton_roche = QPushButton()
        self.bouton_roche.setObjectName("roche")
        self.bouton_roche.setFixedSize(grandeur_bouton)
        self.roche_pixmap = QPixmap("roche.png").scaled(QSize(64, 64))
        self.bouton_roche.setIcon(self.roche_pixmap)
        self.bouton_roche.clicked.connect(self.jouer_clicked)
        self.disposition_joueur.addWidget(self.bouton_roche)

        self.bouton_papier = QPushButton()
        self.bouton_papier.setObjectName("papier")
        self.bouton_papier.setFixedSize(grandeur_bouton)
        self.papier_pixmap = QPixmap("papier.png").scaled(QSize(64, 64))
        self.bouton_papier.setIcon(self.papier_pixmap)
        self.bouton_papier.clicked.connect(self.jouer_clicked)
        self.disposition_joueur.addWidget(self.bouton_papier)

        self.bouton_ciseaux = QPushButton()
        self.bouton_ciseaux.setObjectName("ciseaux")
        self.bouton_ciseaux.setFixedSize(grandeur_bouton)
        self.ciseaux_pixmap = QPixmap("ciseaux.png").scaled(QSize(64, 64))
        self.bouton_ciseaux.setIcon(self.ciseaux_pixmap)
        self.bouton_ciseaux.clicked.connect(self.jouer_clicked)
        self.disposition_joueur.addWidget(self.bouton_ciseaux)

        self.disposition.addLayout(self.disposition_joueur, 1, 1, 3, 1)

        self.log_jeu = QTextEdit()
        self.disposition.addWidget(self.log_jeu, 1, 2, 3, 1)

        self.choix_ordi = QLabel()
        self.disposition.addWidget(self.choix_ordi, 1, 3, 3, 1)

    def jouer_clicked(self):
        sender = self.sender()
        nom = sender.objectName()

        resultat, choix_cpu = partie_rpc(nom)

        if choix_cpu == "roche":
            self.choix_ordi.setPixmap(self.roche_pixmap)
        elif choix_cpu == "papier":
            self.choix_ordi.setPixmap(self.papier_pixmap)
        else:
            self.choix_ordi.setPixmap(self.ciseaux_pixmap)

        self.log_jeu.append(f"Choix de l'ordi: {choix_cpu}")

        if resultat == 0:
            self.log_jeu.append("Vous avez perdu")
        elif resultat == 1:
            self.log_jeu.append("Vous avez gagné")
        else:
            self.log_jeu.append("Partie nulle")


app = QApplication()
rpc = JeuRochePapierCiseaux()
rpc.show()
app.exec()


