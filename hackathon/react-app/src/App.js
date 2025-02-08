import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
	const [modelType, setModelType] = useState("");
	const [vehicleType, setVehicleType] = useState("");
	const [trannyType, setTrannyType] = useState("");
	const [fuelType, setFuelType] = useState("");
	const [predVal, setPredVal] = useState("");
	const [engineSize, setEngineSize] = useState("");
	const [engineCylinders, setEngineCylinders] = useState("");

	useEffect(() => {
		fetch(`http://127.0.0.1:5000/init`);
	}, []);

	const handleDropdownModelType = event => {
		setModelType(event.target.value);
	};
	const handleDropdownVehicleType = event => {
		setVehicleType(event.target.value);
	};
	const handleDropdownTrannyType = event => {
		setTrannyType(event.target.value);
	};
	const handleDropdownFuelType = event => {
		setFuelType(event.target.value);
	};
	const handleEngineSizeChange = event => {
		setEngineSize(event.target.value);
	};
	const handleEngineCylindersChange = event => {
		setEngineCylinders(event.target.value);
	};

	const handleSubmit = () => {
		fetch(
			`http://127.0.0.1:5000/predict?type=${modelType}&vehicleclass=${vehicleType}&enginesize=${engineSize}&cylinders=${engineCylinders}&transmission=${trannyType}&fueltype={fuelType}`,
		).then(res => {
			res.json().then(res => {
				setPredVal("Loading...");
				setTimeout(() => setPredVal(res.result.toFixed(2) + " " + (modelType === "co2" ? "g/km" : "MPG")), 500);
			});
		});
	};
	return (
		<div className="App">
			<form>
				{/* Dropdown menu */}
				<label htmlFor="dropdown">Choose what variable to predict:</label>
				<select id="dropdown" value={modelType} onChange={handleDropdownModelType}>
					<option value="">--Select--</option>
					<option value="co2">Predict CO2 Emissions</option>
					<option value="mpg">Predict MPG of Vehicle</option>
				</select>

				{/* Other input fields */}
				<label htmlFor="dropdown2">Vehicle Class:</label>
				<select id="dropdown2" value={vehicleType} onChange={handleDropdownVehicleType}>
					<option value="">--Select--</option>
					<option value="PICKUP TRUCK - STANDARD">PICKUP TRUCK - STANDARD</option>
					<option value="VAN - CARGO">VAN - CARGO</option>
					<option value="MINIVAN">MINIVAN</option>
					<option value="SPECIAL PURPOSE VEHICLE">SPECIAL PURPOSE VEHICLE</option>
					<option value="STATION WAGON - SMALL">STATION WAGON - SMALL</option>
					<option value="STATION WAGON - MID-SIZE">STATION WAGON - MID-SIZE</option>
					<option value="SUV - SMALL">SUV - SMALL</option>
					<option value="VAN - PASSENGER">VAN - PASSENGER</option>
					<option value="MINICOMPACT">MINICOMPACT</option>
					<option value="TWO-SEATER">TWO-SEATER</option>
					<option value="SUBCOMPACT">SUBCOMPACT</option>
					<option value="PICKUP TRUCK - SMALL">PICKUP TRUCK - SMALL</option>
					<option value="SUV - STANDARD">SUV - STANDARD</option>
					<option value="COMPACT">COMPACT</option>
					<option value="MID-SIZE">MID-SIZE</option>
					<option value="FULL-SIZE">FULL-SIZE</option>
				</select>

				<label htmlFor="input3">Engine Size:</label>
				<input type="text" id="input3" value={engineSize} onChange={handleEngineSizeChange} />

				{/* Number of Engine Cylinders Input */}
				<label htmlFor="input4">Number of Engine Cylinders:</label>
				<input
					type="text"
					id="input4"
					value={engineCylinders} // Bind value to React state
					onChange={handleEngineCylindersChange} // Update state when the user types
				/>

				<label htmlFor="dropdown3">Transmission Type:</label>
				<select id="dropdown3" value={trannyType} onChange={handleDropdownTrannyType}>
					<option value="">--Select--</option>
					<option value="AM8">AM8</option>
					<option value="AS10">AS10</option>
					<option value="AV">AV</option>
					<option value="AS5">AS5</option>
					<option value="M5">M5</option>
					<option value="A4">A4</option>
					<option value="A6">A6</option>
					<option value="AM5">AM5</option>
					<option value="AS7">AS7</option>
					<option value="A8">A8</option>
					<option value="AS4">AS4</option>
					<option value="AM9">AM9</option>
					<option value="AS8">AS8</option>
					<option value="AS9">AS9</option>
					<option value="A5">A5</option>
					<option value="AS6">AS6</option>
					<option value="A10">A10</option>
					<option value="M6">M6</option>
					<option value="A7">A7</option>
					<option value="AV10">AV10</option>
					<option value="AV8">AV8</option>
					<option value="M7">M7</option>
					<option value="A9">A9</option>
					<option value="AV7">AV7</option>
					<option value="AM7">AM7</option>
					<option value="AV6">AV6</option>
					<option value="AM6">AM6</option>
				</select>

				<label htmlFor="dropdown4">Fuel Type:</label>
				<select id="dropdown4" value={fuelType} onChange={handleDropdownFuelType}>
					<option value="">--Select--</option>
					<option value="Z">premium gasoline</option>
					<option value="D">diesel</option>
					<option value="E">ethanol (E85)</option>
					<option value="N">natural gas</option>
				</select>
			</form>
			<div className="right-side">
				<button onClick={handleSubmit}>Get Predicted Value</button>
				<p>Value: {predVal}</p>
			</div>
		</div>
	);
}

export default App;
