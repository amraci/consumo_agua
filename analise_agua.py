{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "0867ead1-5444-4792-b034-907cd5fa2184",
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash\n",
    "from dash import dcc, html\n",
    "from dash.dependencies import Input, Output\n",
    "import pandas as pd\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c03aa5a7-7e0f-4042-8b7a-30f070a93f7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_excel('consumo_caesb.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b37bd56b-4f03-4536-8fb5-fa30cb0ea0cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = dash.Dash(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "14ef2817-fa2d-4bd3-b559-b88ea407451f",
   "metadata": {},
   "outputs": [],
   "source": [
    "app.layout = html.Div([\n",
    "    html.H1(\"Dashboard de Consumo de Água\"),\n",
    "    dcc.Dropdown(\n",
    "        id='tipo-consumo',\n",
    "        options=[\n",
    "           # {'label': 'Consumo Total', 'value': 'total'},\n",
    "            {'label': 'Consumo Médio', 'value': 'medio'},\n",
    "        ],\n",
    "        value='medio'\n",
    "    ),\n",
    "    dcc.Dropdown(\n",
    "        id='filtro-unidade',\n",
    "        options=[{'label': unidade, 'value': unidade} for unidade in df['Sigla'].unique()],\n",
    "        value=df['Sigla'].unique()[0],  # Valor padrão\n",
    "        multi=False\n",
    "    ),\n",
    "    dcc.Graph(id='grafico-consumo')\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8e7efe1b-5e21-466d-8c25-9f840e613416",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.callback(\n",
    "    Output('grafico-consumo', 'figure'),\n",
    "    [Input('tipo-consumo', 'value'),\n",
    "     Input('filtro-unidade', 'value')]\n",
    ")\n",
    "def atualizar_grafico(tipo, unidade):\n",
    "    # Filtrar o dataframe pela unidade selecionada\n",
    "    df_filtrado = df[df['Sigla'] == unidade]\n",
    "\n",
    "    #if tipo == 'total':\n",
    "    #    fig = px.line(df_filtrado, x='Comp', y='Metro', title=f'Consumo Total de Água - {unidade}')                 \n",
    "    #else:\n",
    "    media = df_filtrado['Metro'].median()\n",
    "    fig = px.bar(df_filtrado, x='Comp', y='Metro', title=f'Consumo Médio de Água - {unidade}', \n",
    "                     text=df_filtrado['Metro'].apply(lambda x: f'{x/media:.2%}'))     \n",
    "               \n",
    "\n",
    "     # Adicionando a linha da média\n",
    "    fig.add_hline(y=media, line_dash=\"dash\", line_color=\"red\", \n",
    "                      annotation_text=\"Mediana\", annotation_position=\"bottom right\")\n",
    "        \n",
    "    return fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e7a721d9-7d42-416a-a26b-0fc9a88138bc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x29ff43d9af0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53ba8d1e-86f9-44c3-aaf4-f217b661e45c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
