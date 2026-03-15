from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# 教授，这是你要的“黑金实战”前端界面
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>加密教授 | AI 策略终端</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #0d1117; color: #e6edf3; }
        .gold-border { border: 1px solid #d4af37; box-shadow: 0 0 15px rgba(212, 175, 55, 0.2); }
        .gold-text { color: #d4af37; }
        .btn-gold { background: linear-gradient(145deg, #d4af37, #b8860b); color: #000; font-weight: 900; }
    </style>
</head>
<body class="p-8">
    <div class="max-w-5xl mx-auto">
        <div class="gold-border rounded-xl p-8 bg-gray-900 mb-8 text-center">
            <h1 class="text-4xl font-black gold-text mb-4">📊 AI 智能实盘分析系统</h1>
            <button onclick="runAnalysis()" class="btn-gold px-12 py-4 rounded-full text-xl hover:scale-105 transition">
                开启 AI 深度分析
            </button>
        </div>
        <div id="resultBox" class="hidden gold-border rounded-lg p-6 bg-black min-h-[400px]">
            <div id="status" class="gold-text animate-pulse text-lg mb-4">正在计算 TD 序列与 EMA 交叉...</div>
            <div id="content" class="text-gray-300 whitespace-pre-wrap leading-relaxed"></div>
        </div>
    </div>
    <script>
        async function runAnalysis() {
            const box = document.getElementById('resultBox');
            const content = document.getElementById('content');
            box.classList.remove('hidden');
            content.innerText = "";
            try {
                const res = await fetch('/api/app?action=analyze'); // 还是请求自己
                const data = await res.json();
                document.getElementById('status').innerText = "✅ 分析完成 (Gemini Pro)";
                content.innerText = data.message;
            } catch (e) { content.innerText = "连接超时，请重试"; }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    # 直接返回 HTML，不给 Vercel 误判的机会
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/app')
def handle_request():
    # 你的原有的 Gemini/Tushare 分析逻辑
    return jsonify({"status": "success", "message": "分析完成"})
