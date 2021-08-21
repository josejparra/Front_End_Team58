import dash
import dash_bootstrap_components as dbc 

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, 
                external_stylesheets = [dbc.themes.LITERA],
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

index_long = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rionegro: Taxes Revenue Forecast</title>
    <link rel="icon" href="{{ url_for('static', filename='img/favicon.svg') }}" sizes="any" type="image/svg+xml">
    <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/litera/bootstrap.min.css">
    <!--link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/sketchy/bootstrap.min.css"-->
    <link rel="stylesheet" href="{{ url_for('static',filename='style.css') }}">    
</head>
<body>
  <div class="row">
		<div class="col-md-3 my-auto">
      <img src="https://rionegro.gov.co/wp-content/themes/rionegro/img/logo-rionegro.svg" class="img-fluid" width="260px">
    </div>
		<div class="col-md-6 my-auto">
			<h1>Taxes Revenue Forecast Dashboard</h1>
		</div>
		<div class="col-md-3 my-auto">
			<img src="https://www.correlation-one.com/hubfs/c1logo_color.png" class="img-fluid" width="260px">
    </div>
	</div>  
    {%app_entry%}
        <footer>
    {%config%}
    {%scripts%}
    {%renderer%}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>    
</body>
</html>
'''

#app.index_string=index_long
