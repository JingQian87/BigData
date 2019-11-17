function HW4_Q1(){
	var data = [80, 100, 56, 120, 180, 30, 40, 120, 160];
    var svgWidth = 500, svgHeight = 300;
    // The required padding between bars is 5px.
    // The label must locate 2px above the middle of each bar.

    var svg = d3.select('svg')
            .attr("width", svgWidth)
            .attr("height", svgHeight);

    var barChart = svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .attr("transform", function(d, i) { return "translate(" + i * 55 + ","+(svgHeight-d)+")"; })
            .attr('width', 50)
            .attr('height', svgHeight)
            .attr("fill", "#C0C0C0");

    var text = svg.selectAll(".textlabel")
            .data(data)
            .enter()
            .append("text")
            .attr("class", "textlabel")
            .attr("transform", function(d, i) { return "translate(" + (i * 55+25) + ","+(svgHeight-d-2)+")"; })
            .attr("text-anchor", "middle")
            .style("font-family", "Arial")
            .style("color", "#333333")
            .text(function(d){return d;});
}