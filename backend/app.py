"""
BatteryGuard Flask Application
================================
Main entry point for the backend API server.
"""
import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

from routes.battery  import battery_bp
from routes.analysis import analysis_bp
from routes.anomaly  import anomaly_bp
from routes.rag      import rag_bp

app = Flask(__name__)

# Allow Vite dev server origin
CORS(app, origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
])

# Register blueprints
app.register_blueprint(battery_bp,  url_prefix='/api')
app.register_blueprint(analysis_bp, url_prefix='/api')
app.register_blueprint(anomaly_bp,  url_prefix='/api')
app.register_blueprint(rag_bp,      url_prefix='/api')


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'service': 'BatteryGuard API', 'version': '1.0.0'})


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error', 'detail': str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'
    print(f"[BatteryGuard] Starting API server on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=debug)
