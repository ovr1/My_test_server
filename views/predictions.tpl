<html><head>
  <meta charset='utf-8'>
  <title>Гороскоп на сегодня</title>

  <body>
    <div class="container">
      <h1>Что день {{ date }} готовит</h1>

      % for pred in predictions:
      <p>{{ pred }}</p>
      % end

    </div>
  </body>
  <script language="javascript">
    console.log( {{ x }} );
  </script>
</html>