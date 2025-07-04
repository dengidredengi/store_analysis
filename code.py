import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

os.makedirs('graphs', exist_ok=True)
df = pd.read_csv('data/sample_superstore.csv', encoding='latin1', parse_dates=['Order Date', 'Ship Date'])

print(df.info())

# Вычисляем среднее ROI во всем датасете до 2 знаков после запятой 
# mean() возвращает среднее арифмитическое
df['ROI'] = df['Profit'] / df['Sales']
print(f"Среднее значение ROI: {df['ROI'].mean():.2f}")

# Группировка ROI по категориям и регионам, вычисляем среднее значение ROI для каждой категории и региона
roi_by_category = df.groupby('Category')['ROI'].mean().sort_values(ascending=False)
roi_by_region = df.groupby('Region')['ROI'].mean().sort_values(ascending=False)
print('ROI по категориям', roi_by_category)
print('ROI по регионам', roi_by_region)

# Построение графиков среднего ROI
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
roi_by_category.plot(kind='line', marker='o', color='skyblue')
plt.title('Средний ROI по категориям')
plt.ylabel('ROI')
plt.xticks(rotation=0)

plt.subplot(1, 2, 2)
roi_by_region.plot(kind='line', marker='o', color='lightgreen')
plt.title('Средний ROI по регионам')
plt.ylabel('ROI')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('graphs/roi_analysis.png')
plt.show()


# Найдем 10 самых прибыльных товаров
top_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
print('Топ 10 самых прибыльных товаров:')
print(top_products)

# Найдем 10 самых убыточных товаров
low_profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=True).head(10)
print('Топ 10 самых убыточных товаров:')
print(low_profit_products)