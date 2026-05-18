import { useEffect, useState } from "react";
import axios from "axios";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  PieChart,
  Pie,
  Cell
} from "recharts";

function App() {

  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {

    const city = await axios.get(
      "http://127.0.0.1:8000/city-count"
    );

    const category = await axios.get(
      "http://127.0.0.1:8000/category-count"
    );

    const source = await axios.get(
      "http://127.0.0.1:8000/source-count"
    );

    setCityData(city.data);
    setCategoryData(category.data);
    setSourceData(source.data);
  };

  return (

    <div style={{
      padding: "30px",
      fontFamily: "Arial",
      backgroundColor: "#f1f5f9",
      minHeight: "100vh"
    }}>

      <h1 style={{
        textAlign: "center",
        color: "#0f172a",
        marginBottom: "40px"
      }}>
        Business Listings Dashboard
      </h1>

      <div style={{
        background: "white",
        padding: "20px",
        borderRadius: "12px",
        marginBottom: "30px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
      }}>

        <h2>City Wise Count</h2>

        <BarChart
          width={1000}
          height={300}
          data={cityData}
        >
          <XAxis dataKey="city" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="total" fill="#6366f1" />
        </BarChart>

      </div>

      <div style={{
        background: "white",
        padding: "20px",
        borderRadius: "12px",
        marginBottom: "30px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
      }}>

        <h2>Category Wise Count</h2>

        <BarChart
          width={1000}
          height={300}
          data={categoryData}
        >
          <XAxis dataKey="category" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="total" fill="#22c55e" />
        </BarChart>

      </div>

      <div style={{
        background: "white",
        padding: "20px",
        borderRadius: "12px",
        boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
      }}>

        <h2>Source Wise Count</h2>

        <PieChart width={500} height={400}>

          <Pie
            data={sourceData}
            dataKey="total"
            nameKey="source"
            outerRadius={120}
            fill="#8884d8"
            label
          >

            {sourceData.map((entry, index) => (
              <Cell key={index} />
            ))}

          </Pie>

          <Tooltip />

        </PieChart>

      </div>

    </div>
  );
}

export default App;