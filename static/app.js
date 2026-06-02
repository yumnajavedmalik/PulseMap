
function loadMap() {

    const data = [{
        type: "choropleth",
        locationmode: "country names",

       
        locations: [
            "Pakistan", "India", "United States", "Germany", "Japan",
            "China", "France", "United Kingdom", "Brazil", "Canada",
            "Australia", "Russia", "South Africa", "Italy", "Spain"
        ],

        z: [
            0.2, -0.1, 0.4, 0.3, 0.1,
            -0.2, 0.35, 0.25, -0.15, 0.3,
            0.05, -0.3, 0.1, 0.2, 0.15
        ],

        zmin: -0.5,
        zmax: 0.5,

        colorscale: [
            [0, "#d73027"],     // red (negative)
            [0.5, "#ffffbf"],   // yellow (neutral)
            [1, "#1a9850"]      // green (positive)
        ],

        colorbar: {
            title: "Sentiment",
            tickvals: [-0.5, 0, 0.5]
        },

        hovertemplate:
            "<b>%{location}</b><br>Sentiment: %{z}<extra></extra>"
    }];

    const layout = {
        title: {
            text: "🌍 Global News Sentiment Heatmap",
            font: { size: 22 }
        },

        geo: {
            projection: { type: "natural earth" },
            showframe: false,
            showcoastlines: false,
            bgcolor: "rgba(0,0,0,0)"
        },

        margin: { t: 50, l: 0, r: 0, b: 0 },

        paper_bgcolor: "white"
    };

    Plotly.newPlot("map", data, layout, { responsive: true });
}

loadMap();


async function searchCountry() {

    let name = document.getElementById("search").value;

    document.getElementById("error").innerText = "";

    try {

        let res = await fetch(`/api/country/${name}`);

        let data = await res.json();

        if (!res.ok) {
            document.getElementById("error").innerText = data.error;
            return;
        }

        document.getElementById("stats").innerHTML = `
            <h4>${data.country}</h4>
            <p><b>Sentiment:</b> ${data.sentiment}</p>
            <h5>Top Headlines:</h5>
            <ul>
                ${data.articles.map(a => `<li>${a}</li>`).join("")}
            </ul>
        `;

    } catch (err) {
        document.getElementById("error").innerText = "Server error";
    }
}