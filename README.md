# 🎮 迷宮解決方案專案 (Maze Solution Project)

一個使用 Python 和 Pygame 開發的互動式迷宮遊戲，集成了多種經典的迷宮路徑尋找演算法，提供視覺化學習體驗。

## 📋 專案特色

### 🎯 雙重遊戲模式
- **手動模式 (Manual Solve)**: 玩家使用方向鍵控制角色在迷宮中移動
- **自動模式 (Auto Solve)**: 選擇不同演算法自動解決迷宮

### 🧠 六種路徑尋找演算法
1. **BFS (廣度優先搜尋)** - 保證找到最短路徑
2. **DFS (深度優先搜尋)** - 快速但可能不是最短路徑
3. **Dijkstra** - 考慮權重的單源最短路徑演算法
4. **A* (A-Star)** - 使用啟發式函數的最優化搜尋
5. **Wall Follower** - 沿牆行走的經典迷宮解法
6. **Dead End Filling** - 填滿死路來簡化迷宮

### 🎨 視覺化特色
- **即時動畫**: 每個演算法都有視覺化動畫，展示搜尋過程
- **顏色編碼**: 不同狀態用不同顏色表示（已訪問、當前位置、路徑等）
- **互動式介面**: 滑鼠懸停效果和清晰的選單系統
- **警告提示**: 演算法執行前會顯示等待提示

## 🏗️ 專案架構

```
mazeSolution/
├── main.py                 # 主程式入口
├── config.py              # 全域配置設定
├── map.py                 # 迷宮地圖類別
├── screen_display.py      # 使用者介面管理
├── sprite.py              # 遊戲精靈（玩家和目標點）
├── BFS.py                 # 廣度優先搜尋演算法
├── DFS.py                 # 深度優先搜尋演算法
├── Dijkstra.py            # Dijkstra 最短路徑演算法
├── AStar.py               # A* 啟發式搜尋演算法
├── WallFollower.py        # 牆跟隨演算法
├── DeadEndFilling.py      # 死路填充演算法
├── requirements.txt       # 專案依賴
└── README.md              # 專案說明文件
```

## ⚙️ 技術規格

- **開發語言**: Python 3.x
- **圖形庫**: Pygame 2.5.2
- **迷宮尺寸**: 15×15 網格
- **單元格大小**: 40×40 像素
- **起始位置**: (1,1)
- **目標位置**: (1,11)

## 🚀 安裝與運行

### 環境要求
- Python 3.6 或更高版本
- pip 套件管理器

### 安裝步驟

1. **克隆專案**
   ```bash
   git clone <repository-url>
   cd mazeSolution
   ```

2. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

3. **執行程式**
   ```bash
   python main.py
   ```

## 🐞 VS Code 除錯設定

`.vscode/` 已被加入 `.gitignore`，不會納入版控（其中包含與本機環境相關的 Python 直譯器路徑）。若要在 VS Code 中進行除錯，請於專案根目錄自行建立 `.vscode/launch.json`：

```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: main.py",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/main.py",
      // 改成你本機的 Python 直譯器路徑（建議使用安裝了 pygame 的虛擬環境）
      "python": "/path/to/your/python",
      "console": "integratedTerminal"
    }
  ]
}
```

設定步驟：

1. 先安裝 [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 與 [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy) 擴充套件。
2. 用 `which python`（macOS/Linux）或 `where python`（Windows）查出直譯器路徑，填入上方 `python` 欄位。
3. 開啟 `main.py`，按 `F5` 即可開始除錯。

> 💡 也可以直接在 VS Code 開啟 `main.py` 後，點選右上角的「執行與偵錯」並選擇 Python File，VS Code 會自動產生 `launch.json`。

## 🎮 使用說明

### 遊戲操作

1. **啟動遊戲**後會看到主選單
2. **選擇遊戲模式**：
   - `Manual Solve`: 手動控制模式
   - `Auto Solve`: 自動演算法模式
   - `Back`: 返回/退出

3. **手動模式操作**：
   - 使用方向鍵 (↑↓←→) 控制角色移動
   - 到達目標位置即可獲勝

4. **自動模式操作**：
   - 選擇要使用的演算法
   - 觀看演算法動畫演示
   - 等待演算法完成並顯示結果

### 演算法說明

| 演算法 | 特點 | 適用場景 |
|--------|------|----------|
| **BFS** | 保證最短路徑，記憶體使用較多 | 需要最優解時 |
| **DFS** | 記憶體使用少，速度快 | 快速搜尋時 |
| **Dijkstra** | 考慮權重的最短路徑 | 有權重圖時 |
| **A*** | 啟發式搜尋，效率高 | 平衡效率與最優性 |
| **Wall Follower** | 簡單可靠，沿牆行走 | 簡單迷宮 |
| **Dead End Filling** | 預處理迷宮，簡化問題 | 複雜迷宮 |

## 🎨 顏色說明

- **白色**: 可通行區域
- **黑色**: 牆壁/障礙物
- **紅色**: 玩家角色
- **綠色**: 目標位置
- **藍色**: 已訪問的節點
- **黃色**: 當前搜尋位置
- **紫色**: 找到的路徑

## 📚 教育價值

這個專案非常適合：

- **演算法學習**: 視覺化理解不同搜尋策略的差異
- **程式設計教學**: 展示物件導向程式設計和模組化架構
- **遊戲開發入門**: 學習 Pygame 基礎和遊戲循環概念
- **資料結構實踐**: 理解佇列、堆疊、優先佇列等資料結構的應用

## 🔧 自定義設定

您可以通過修改 `config.py` 來自定義：

- 迷宮大小 (`ROWS`, `COLS`)
- 單元格大小 (`CELL_SIZE`)
- 起始和目標位置 (`START`, `GOAL`)
- 顏色配置
- 動畫延遲時間
- 演算法列表

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

1. Fork 本專案
2. 創建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 文件

## 📞 聯絡資訊

如有問題或建議，請透過以下方式聯絡：

- 提交 Issue
- 發送 Email

---

⭐ 如果這個專案對您有幫助，請給個 Star 支持一下！
