# -*- coding: utf-8 -*-

from django.http import HttpResponse


# 接收请求数据
def Process(request):
    request.encoding = 'utf-8'

    type = request.GET['type']  # 類型
    if type in "classify":
        index_col = request.GET['index_col']  # 資料序號
        dep_k = request.GET['dep_k']  # 應變數數量
        ind_k = request.GET['ind_k']  # 自變數數量
        hidden_units = request.GET['hidden_units']  # 隱藏層數目與各隱藏層神經元
        learning_rate = request.GET['learning_rate']  # 學習率
        network_name = request.GET['network_name']  # 網路名稱
        batch = request.GET['batch']  # 訓練批次大小
        max_step = request.GET['max_step']  # 訓練循環
        n_classes = request.GET['n_classes']  # 分類總類數目

        message = "分類模式參數設定=>" + "資料序號:" + index_col + "應變數數量:" + dep_k + "自變數數量:" + ind_k + "隱藏層數目與各隱藏層神經元:" + hidden_units + "學習率:" + learning_rate \
                  + "網路名稱:" + network_name + "訓練批次大小:" + batch + "訓練循環:" + max_step + "分類總類數目:" + n_classes + "類型:" + type
        return HttpResponse(message)

    elif type in "classify_csv":
        file_path = request.GET['file_path']  # 資料檔案路徑(上傳)
        tf_data_path = request.GET['tf_data_path']  # 資料檔案路徑(回傳)
        model_path = request.GET['model_path']  # 模型上傳和回傳路徑
        message = "分類模式CSV=>" + "資料檔案路徑(上傳):" + file_path + "資料檔案路徑(回傳):" + tf_data_path + "模型上傳和回傳路徑:" + model_path + "類型:" + type
        return HttpResponse(message)

    elif type in "prediction":
        index_col = request.GET['index_col']  # 資料序號
        dep_k = request.GET['dep_k']  # 應變數數量
        ind_k = request.GET['ind_k']  # 自變數數量
        hidden_units = request.GET['hidden_units']  # 隱藏層數目與各隱藏層神經元
        learning_rate = request.GET['learning_rate']  # 學習率
        network_name = request.GET['network_name']  # 網路名稱
        batch = request.GET['batch']  # 訓練批次大小
        max_step = request.GET['max_step']  # 訓練循環
        n_classes = request.GET['n_classes']  # 分類總類數目

        message = "分類模式參數設定=>" + "資料序號:" + index_col + "應變數數量:" + dep_k + "自變數數量:" + ind_k + "隱藏層數目與各隱藏層神經元:" + hidden_units + "學習率:" + learning_rate \
                  + "網路名稱:" + network_name + "訓練批次大小:" + batch + "訓練循環:" + max_step + "分類總類數目:" + n_classes + "類型:" + type

        return HttpResponse(message)

    elif type in "prediction_csv":
        file_path = request.GET['file_path']  # 資料檔案路徑(上傳)
        tf_data_path = request.GET['tf_data_path']  # 資料檔案路徑(回傳)
        model_path = request.GET['model_path']  # 模型上傳和回傳路徑
        message = "預測模式CSV=>" + "資料檔案路徑(上傳):" + file_path + "資料檔案路徑(回傳):" + tf_data_path + "模型上傳和回傳路徑:" + model_path + "類型:" + type
        return HttpResponse(message)
