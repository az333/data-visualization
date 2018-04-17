function tooltipHtml(n, d){	/* function to create html content string in tooltip div. */
    return "<h4>"+n+"</h4><table>"+
	"<tr><td>Deaths</td><td>"+(d.deaths)+"</td></tr>"+
	"<tr><td>Rate</td><td>"+(d.rate)+"</td></tr>"+
	"</table>";
}

var data = {'WA': {'RATE': '9', 'DEATHS': '686'}, 'DE': {'RATE': '11', 'DEATHS': '111'}, 'WI': {'RATE': '11.4', 'DEATHS': '664'}, 'WV': {'RATE': '17.5', 'DEATHS': '332'}, 'HI': {'RATE': '4.5', 'DEATHS': '66'}, 'FL': {'RATE': '12.6', 'DEATHS': '2,704'}, 'WY': {'RATE': '17.4', 'DEATHS': '101'}, 'NH': {'RATE': '9.3', 'DEATHS': '132'}, 'NJ': {'RATE': '5.5', 'DEATHS': '485'}, 'NM': {'RATE': '18.1', 'DEATHS': '383'}, 'TX': {'RATE': '12.1', 'DEATHS': '3,353'}, 'LS': {'RATE': '21.3', 'DEATHS': '987'}, 'NC': {'RATE': '13.7', 'DEATHS': '1,409'}, 'ND': {'RATE': '11.9', 'DEATHS': '90'}, 'NE': {'RATE': '9.1', 'DEATHS': '171'}, 'TN': {'RATE': '17.1', 'DEATHS': '1,148'}, 'NY': {'RATE': '4.4', 'DEATHS': '900'}, 'PA': {'RATE': '12', 'DEATHS': '1,555'}, 'CA': {'RATE': '7.9', 'DEATHS': '3,184'}, 'NV': {'RATE': '16.8', 'DEATHS': '498'}, 'VA': {'RATE': '12.1', 'DEATHS': '1,049'}, 'CO': {'RATE': '14.3', 'DEATHS': '812'}, 'AK': {'RATE': '23.3', 'DEATHS': '177'}, 'AL': {'RATE': '21.5', 'DEATHS': '1,046'}, 'AR': {'RATE': '17.8', 'DEATHS': '541'}, 'VT': {'RATE': '11.1', 'DEATHS': '78'}, 'IL': {'RATE': '11.7', 'DEATHS': '1,490'}, 'GA': {'RATE': '15', 'DEATHS': '1,571'}, 'IN': {'RATE': '15', 'DEATHS': '997'}, 'IA': {'RATE': '9.2', 'DEATHS': '288'}, 'OK': {'RATE': '19.6', 'DEATHS': '766'}, 'AZ': {'RATE': '15.2', 'DEATHS': '1,094'}, 'ID': {'RATE': '14.6', 'DEATHS': '242'}, 'CT': {'RATE': '4.6', 'DEATHS': '172'}, 'ME': {'RATE': '8.3', 'DEATHS': '123'}, 'MD': {'RATE': '11.9', 'DEATHS': '707'}, 'MA': {'RATE': '3.4', 'DEATHS': '242'}, 'OH': {'RATE': '12.9', 'DEATHS': '1,524'}, 'UT': {'RATE': '12.9', 'DEATHS': '370'}, 'MO': {'RATE': '19', 'DEATHS': '1,144'}, 'MN': {'RATE': '7.6', 'DEATHS': '432'}, 'MI': {'RATE': '12.3', 'DEATHS': '1,230'}, 'RI': {'RATE': '4.1', 'DEATHS': '49'}, 'KS': {'RATE': '13.4', 'DEATHS': '383'}, 'MT': {'RATE': '18.9', 'DEATHS': '194'}, 'MS': {'RATE': '19.9', 'DEATHS': '587'}, 'SC': {'RATE': '17.7', 'DEATHS': '891'}, 'KY': {'RATE': '17.5', 'DEATHS': '772'}, 'OR': {'RATE': '11.9', 'DEATHS': '513'}, 'SD': {'RATE': '13.4', 'DEATHS': '108'}}


var sampleData ={};	/* Sample random data. */	
["HI", "AK", "FL", "SC", "GA", "AL", "NC", "TN", "RI", "CT", "MA",
 "ME", "NH", "VT", "NY", "NJ", "PA", "DE", "MD", "WV", "KY", "OH", 
 "MI", "WY", "MT", "ID", "WA", "TX", "CA", "AZ", "NV", "UT", 
 "CO", "NM", "OR", "ND", "SD", "NE", "IA", "MS", "IN", "IL", "MN", 
 "WI", "MO", "AR", "OK", "KS", "LS", "VA"]
    .forEach(function(d){
	var deaths=data[d]["DEATHS"], 
	    rate=data[d]["RATE"];
	sampleData[d]={deaths:deaths, rate:rate,
		       avg:rate, color:d3.interpolate("#ffffcc", "#800026")(rate/25)}; 
    });

sampleData["DC"]={deaths:"N/A", rate:"N/A", color:"N/A"};

/* draw states on id #statesvg */	
uStates.draw("#statesvg", sampleData, tooltipHtml);

d3.select(self.frameElement).style("height", "600px");
