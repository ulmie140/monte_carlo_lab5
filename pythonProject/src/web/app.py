from flask import Flask, render_template, request, jsonify
from src.services.simulation import MonteCarloSimulation

app = Flask(__name__)


@app.route("/")
def index():
    """Отображает главную страницу с интерфейсом"""
    return render_template("index.html")


@app.route("/api/simulate", methods=["POST"])
def simulate():
    """Принимает данные от клиента, запускает симуляцию и возвращает результат"""
    data = request.json

    try:
        a_val = float(data.get("a", 5))
        b_val = float(data.get("b", 2))
        c_val = float(data.get("c", 50))
        d_val = float(data.get("d", 150))
        n_val = int(data.get("n", 10000))

        # Используем наш существующий слой бизнес-логики
        sim = MonteCarloSimulation(a_val, b_val, c_val, d_val, n_val)
        results = sim.run_simulation()

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400