/* Plotly.d3.csv('Code/clustered.csv', function(err, rows){

    console.log(rows);

    var data = [];
    for(let i=0;i<rows.length;i++) {
        data.push(rows.map(row => row [i]));
    }

    console.log(data);

    Plotly.newPlot('plotArea',[{
        z: data,
        type: 'scatter3d'
    }]);



}); */


Plotly.d3.csv('Code/clustered.csv', function(err, rows){
function unpack(rows, key) {
	return rows.map(function(row)
    { return row[key]; });}
    
    console.log(rows);
    bedro = unpack(rows, 'bedrooms')

var trace1 = {
	x:unpack(rows, 'house_age'), y: unpack(rows, 'price'), z: unpack(rows, 'city_rank'),
    mode: 'markers',
    hovertemplate: '<b>Price</b>: $%{y:,.2f}' + '<br><b>House Age</b>: %{x}<br>' + '<b>City Rank</b>: %{z}<br>',
	marker: {
		size: unpack(rows, 'bedrooms'),
		line: {
		color: unpack(rows, 'Class'),
        width: 10},
    },
	type: 'scatter3d'
};

/* var trace2 = {
	x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), z: unpack(rows, 'z2'),
	mode: 'markers',
	marker: {
		color: 'rgb(127, 127, 127)',
		size: 12,
		symbol: 'circle',
		line: {
		color: 'rgb(204, 204, 204)',
		width: 1},
		opacity: 0.8},
	type: 'scatter3d'};*/

var data = [trace1];
var layout = {
    color: unpack(rows, 'class'),
    width: 500,
    height: 500,
    margin: {
	l: 0,
	r: 0,
	b: 0,
	t: 0
  }};
Plotly.newPlot('myDiv', data, layout);
});