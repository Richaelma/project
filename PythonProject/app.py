# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/literature")
def literature():
    literature_data = [
        {
            "title": "同位素内标-气相色谱质谱法测定海洋动物体中多溴联苯醚 ",
            "authors": ";孙秀梅;金衍健;宋素平;郝青;朱剑;李铁军;郭远明",
            "link": "https://kns.cnki.net/kcms2/article/abstract?v=i_LPdPvRpB7uXsLuh3G1CVceqpR_bNBQfyJAwxO_Uo06LkrKJ8fiO6yEZm47FB00gdfI7Qpkyufa7-DILa7gh7xV7W40b5J9FPs2QYGPxebzRl5WjU3a7hGCLdl30xqv_1DX5DBRt7ngIhIFocYGvBsuXGNHW11tP_pwTBAute7qQTrdUnTfc9kY6h2eTR_2&uniplatform=NZKPT&language=CHS"
        },
        # 更多文献数据...
    ]
    return render_template("literature.html", data=literature_data)

# app.py 新增路由
@app.route("/data")
def data_page():
    # 可以在此处连接数据库获取真实数据
    sample_data = {
        "name": "南海温度数据集",
        "source": "国家海洋信息中心",
        "download_link": "/static/data/sample-data.csv"
    }
    return render_template("data.html", data=sample_data)

from flask import render_template
import pandas as pd  # 示例使用pandas处理数据

# 海洋数据示例（可替换为真实数据源）
marine_data = [
    {"id": 1, "location": "南海", "temperature": 28.5, "salinity": 34.2, "ph": 8.1},
    {"id": 2, "location": "东海", "temperature": 25.3, "salinity": 33.8, "ph": 8.0}
]

@app.route("/data")
def show_data():
    # 可在此处连接数据库或读取CSV文件
    # df = pd.read_csv("marine_data.csv")
    return render_template("data.html", data=marine_data)

# 正确配置（必须包含 host='0.0.0.0'）
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)