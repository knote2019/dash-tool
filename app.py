import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np

# 初始化Dash应用
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# 定义导航栏样式
navbar_style = {
    'backgroundColor': '#2c3e50',
    'padding': '15px 30px',
    'display': 'flex',
    'justifyContent': 'space-between',
    'alignItems': 'center',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
}

nav_link_style = {
    'color': 'white',
    'textDecoration': 'none',
    'padding': '10px 20px',
    'margin': '0 5px',
    'borderRadius': '5px',
    'transition': 'background-color 0.3s',
    'cursor': 'pointer',
    'display': 'inline-block'
}

nav_link_active_style = {
    **nav_link_style,
    'backgroundColor': '#34495e'
}

content_style = {
    'padding': '30px',
    'backgroundColor': '#ecf0f1',
    'minHeight': 'calc(100vh - 80px)'
}


# 创建导航栏组件
def create_navbar():
    return html.Div([
        html.Div([
            html.H2('📊 Plotly Dashboard', style={
                'color': 'white',
                'margin': '0',
                'fontSize': '24px'
            }),
        ], style={'display': 'flex', 'alignItems': 'center'}),
        html.Div([
            html.Div('首页', id='nav-home', n_clicks=0,
                     style=nav_link_style, className='nav-link'),
            html.Div('图表分析', id='nav-charts', n_clicks=0,
                     style=nav_link_style, className='nav-link'),
            html.Div('数据表格', id='nav-data', n_clicks=0,
                     style=nav_link_style, className='nav-link'),
            html.Div('关于', id='nav-about', n_clicks=0,
                     style=nav_link_style, className='nav-link'),
        ], style={'display': 'flex'})
    ], style=navbar_style)


# 首页内容
def home_page():
    return html.Div([
        html.H1('欢迎来到Plotly演示页面', style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'marginBottom': '30px'
        }),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('📈 数据可视化', style={'color': '#3498db'}),
                    html.P('使用Plotly创建交互式图表，支持缩放、悬停等功能'),
                ], style={
                    'backgroundColor': 'white',
                    'padding': '30px',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                    'margin': '10px'
                }),
                html.Div([
                    html.H3('🎨 美观界面', style={'color': '#e74c3c'}),
                    html.P('现代化的设计风格，响应式布局，完美适配各种设备'),
                ], style={
                    'backgroundColor': 'white',
                    'padding': '30px',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                    'margin': '10px'
                }),
                html.Div([
                    html.H3('⚡ 高性能', style={'color': '#2ecc71'}),
                    html.P('基于React和Plotly.js，提供流畅的用户体验'),
                ], style={
                    'backgroundColor': 'white',
                    'padding': '30px',
                    'borderRadius': '10px',
                    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                    'margin': '10px'
                }),
            ], style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(auto-fit, minmax(300px, 1fr))',
                'gap': '20px',
                'marginTop': '30px'
            })
        ])
    ])


# 图表分析页面
def charts_page():
    # 生成示例数据
    np.random.seed(42)
    df = pd.DataFrame({
        '日期': pd.date_range('2024-01-01', periods=30),
        '销售额': np.random.randint(1000, 5000, 30),
        '访问量': np.random.randint(500, 2000, 30)
    })

    # 创建折线图
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(
        x=df['日期'],
        y=df['销售额'],
        mode='lines+markers',
        name='销售额',
        line=dict(color='#3498db', width=3),
        marker=dict(size=8)
    ))
    line_fig.update_layout(
        title='30天销售趋势',
        xaxis_title='日期',
        yaxis_title='销售额 (元)',
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    # 创建柱状图
    bar_fig = px.bar(
        df.tail(10),
        x='日期',
        y='访问量',
        title='最近10天访问量',
        color='访问量',
        color_continuous_scale='Viridis'
    )
    bar_fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    # 创建饼图
    categories = ['电子产品', '服装', '食品', '图书', '其他']
    values = [35, 25, 20, 15, 5]
    pie_fig = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=0.4,
        marker=dict(colors=['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6'])
    )])
    pie_fig.update_layout(
        title='销售分类占比',
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return html.Div([
        html.H1('图表分析', style={'color': '#2c3e50', 'marginBottom': '30px'}),
        html.Div([
            html.Div([
                dcc.Graph(figure=line_fig)
            ], style={
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                'marginBottom': '20px'
            }),
            html.Div([
                html.Div([
                    dcc.Graph(figure=bar_fig)
                ], style={'flex': '1', 'marginRight': '10px'}),
                html.Div([
                    dcc.Graph(figure=pie_fig)
                ], style={'flex': '1', 'marginLeft': '10px'}),
            ], style={
                'display': 'flex',
                'gap': '20px',
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
            })
        ])
    ])


# 数据表格页面
def data_page():
    # 生成示例数据
    df = pd.DataFrame({
        '产品名称': ['产品A', '产品B', '产品C', '产品D', '产品E'],
        '销售额': [15000, 23000, 18000, 31000, 12000],
        '库存': [150, 230, 180, 310, 120],
        '状态': ['正常', '正常', '预警', '正常', '预警']
    })

    # 创建表格图表
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=list(df.columns),
            fill_color='#3498db',
            font=dict(color='white', size=14),
            align='center',
            height=40
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color=[['#ecf0f1' if i % 2 == 0 else 'white' for i in range(len(df))]],
            align='center',
            height=35,
            font=dict(size=13)
        )
    )])
    fig.update_layout(
        title='产品数据总览',
        height=400
    )

    return html.Div([
        html.H1('数据表格', style={'color': '#2c3e50', 'marginBottom': '30px'}),
        html.Div([
            dcc.Graph(figure=fig),
            html.Div([
                html.H3('数据统计', style={'color': '#2c3e50'}),
                html.P(f'总销售额: {df["销售额"].sum():,} 元'),
                html.P(f'总库存: {df["库存"].sum():,} 件'),
                html.P(f'产品种类: {len(df)} 种'),
            ], style={
                'marginTop': '20px',
                'padding': '20px',
                'backgroundColor': '#3498db',
                'color': 'white',
                'borderRadius': '10px'
            })
        ], style={
            'backgroundColor': 'white',
            'padding': '30px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
        })
    ])


# 关于页面
def about_page():
    return html.Div([
        html.H1('关于本项目', style={'color': '#2c3e50', 'marginBottom': '30px'}),
        html.Div([
            html.H3('🚀 技术栈', style={'color': '#3498db'}),
            html.Ul([
                html.Li('Plotly - 交互式图表库'),
                html.Li('Dash - Python Web应用框架'),
                html.Li('Pandas - 数据处理'),
                html.Li('NumPy - 数值计算'),
            ], style={'fontSize': '16px', 'lineHeight': '2'}),

            html.H3('✨ 功能特点', style={'color': '#3498db', 'marginTop': '30px'}),
            html.Ul([
                html.Li('响应式导航栏设计'),
                html.Li('多页面切换功能'),
                html.Li('交互式数据可视化'),
                html.Li('现代化UI设计'),
            ], style={'fontSize': '16px', 'lineHeight': '2'}),

            html.Div([
                html.P('💡 这是一个Plotly + Dash演示项目，展示了如何创建带有导航栏的现代化Web应用。'),
            ], style={
                'marginTop': '30px',
                'padding': '20px',
                'backgroundColor': '#2ecc71',
                'color': 'white',
                'borderRadius': '10px',
                'fontSize': '16px'
            })
        ], style={
            'backgroundColor': 'white',
            'padding': '30px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
        })
    ])


# 应用布局
app.layout = html.Div([
    dcc.Store(id='current-page', data='home'),
    create_navbar(),
    html.Div(id='page-content', style=content_style)
])


# 回调函数：处理导航点击和页面切换
@app.callback(
    [Output('page-content', 'children'),
     Output('nav-home', 'style'),
     Output('nav-charts', 'style'),
     Output('nav-data', 'style'),
     Output('nav-about', 'style'),
     Output('current-page', 'data')],
    [Input('nav-home', 'n_clicks'),
     Input('nav-charts', 'n_clicks'),
     Input('nav-data', 'n_clicks'),
     Input('nav-about', 'n_clicks')],
    prevent_initial_call=False
)
def update_page(home_clicks, charts_clicks, data_clicks, about_clicks):
    ctx = dash.callback_context

    # 默认显示首页
    if not ctx.triggered:
        return home_page(), nav_link_active_style, nav_link_style, nav_link_style, nav_link_style, 'home'

    # 获取触发的按钮ID
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # 根据点击的按钮返回对应页面和样式
    if button_id == 'nav-home':
        return (home_page(),
                nav_link_active_style, nav_link_style, nav_link_style, nav_link_style,
                'home')
    elif button_id == 'nav-charts':
        return (charts_page(),
                nav_link_style, nav_link_active_style, nav_link_style, nav_link_style,
                'charts')
    elif button_id == 'nav-data':
        return (data_page(),
                nav_link_style, nav_link_style, nav_link_active_style, nav_link_style,
                'data')
    elif button_id == 'nav-about':
        return (about_page(),
                nav_link_style, nav_link_style, nav_link_style, nav_link_active_style,
                'about')

    # 默认返回首页
    return home_page(), nav_link_active_style, nav_link_style, nav_link_style, nav_link_style, 'home'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8050)

