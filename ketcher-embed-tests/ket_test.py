from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os

class KetcherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ketcher Integration with PyQt5")
        self.setGeometry(100, 100, 1024, 768)

        # Central widget
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Ketcher embedded in QWebEngineView
        self.web_view = QWebEngineView()
        ketcher_path = os.path.abspath("../ketcher-standalone-2.26.0/standalone/index.html")  # Update with your path
        print(ketcher_path)
        self.web_view.setUrl(QUrl.fromLocalFile(ketcher_path))
        layout.addWidget(self.web_view)

        # Button to retrieve molecule data
        get_data_button = QPushButton("Get Molecule Data")
        get_data_button.clicked.connect(self.get_molecule_data)
        layout.addWidget(get_data_button)

        # Button to send molecule data
        send_data_button = QPushButton("Load Molecule")
        send_data_button.clicked.connect(self.load_molecule)
        layout.addWidget(send_data_button)

    def get_molecule_data(self):
        """
        Retrieve molecule data (e.g., as MOL or SMILES) from Ketcher.
        """
        js_script = "ketcher.getMolfile().then((molfile) => { molfile });"
        self.web_view.page().runJavaScript(js_script, self.handle_molecule_data)

    def handle_molecule_data(self, molfile):
        """
        Handle the molecule data received from Ketcher.
        """
        if molfile:
            print("Molecule Data (MOL):")
            print(molfile)

    def load_molecule(self):
        """
        Send molecule data to Ketcher for rendering.
        """
        sample_molfile = """
          Ketcher  2  3D

          4  3  0  0  0  0            999 V2000
           -0.7500    0.6500    0.0000 C   0  0
            0.7500    0.6500    0.0000 O   0  0
            0.0000   -0.6500    0.0000 C   0  0
           -0.7500   -1.9500    0.0000 C   0  0
          1  2  1  0  0  0  0
          1  3  1  0  0  0  0
          3  4  1  0  0  0  0
        M  END
        """
        js_script = f"ketcher.setMolecule('{sample_molfile}')"
        self.web_view.page().runJavaScript(js_script)

if __name__ == "__main__":
    app = QApplication([])
    window = KetcherApp()
    window.show()
    app.exec_()

