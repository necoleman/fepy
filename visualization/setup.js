    
function makeData(){

	var data = new google.visualization.DataTable();
	data.addColumn('number', '

}

function setup(){

  var numRows = 45.0;
  var numCols = 45;
        
  var tooltipStrings = new Array();
  var data = new google.visualization.DataTable();
        
  for (var i = 0; i < numCols; i++)
  {
    data.addColumn('number', 'col'+i);
  }
        
  data.addRows(numRows);
  var d = 360 / numRows;
  var idx = 0;
        
  for (var i = 0; i < numRows; i++) 
  {
    for (var j = 0; j < numCols; j++)
    {
      var value = (Math.cos(i * d * Math.PI / 180.0) * Math.cos(j * d * Math.PI / 180.0));
      data.setValue(i, j, value / 4.0);

      tooltipStrings[idx] = "x:" + i + ", y:" + j + " = " + value;
      idx++;
    }
  }
	return data;
}
