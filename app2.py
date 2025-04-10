from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    er = None
    if request.method == "POST":
        try:
            Suka = int(request.form["Suka"])
            Komentar = int(request.form["Komen"])
            Bagikan = int(request.form["Bagikan"])
            Pengikut = int(request.form["Pengikut"])

            if Pengikut == 0:
                return "Jumlah pengikut tidak boleh 0!"
            
            # Hitung Engagement Rate
            er = ((Suka + Komentar + Bagikan) / Pengikut) * 100
        
        except ValueError:
            return "Ups! Sepertinya ada yang salah. Coba masukkan angka yang benar."
        
    return render_template("index.html", er=round(er, 2) if er is not None else None)

if __name__ == "__main__":
    app.run(debug=True)
