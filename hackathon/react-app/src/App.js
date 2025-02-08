import React, { useState } from "react";
import "./App.css";

function App() {
	const [modelType, setModelType] = useState("");
	const [vehicleType, setVehicleType] = useState("");

	const handleDropdownModelType = event => {
		setModelType(event.target.value);
	};

	const handleDropdownVehicleType = event => {
		setVehicleType(event.target.value);
	};
	return (
		<div className="App">
			<form>
				{/* Dropdown menu */}
				<label htmlFor="dropdown">Choose an option:</label>
				<select id="dropdown" value={modelType} onChange={handleDropdownModelType}>
					<option value="">--Select--</option>
					<option value="co2">Predict CO2 Emissions</option>
					<option value="mpg">Predict MPG of Vehicle</option>
				</select>

				{/* Other input fields */}
				<label htmlFor="input2">Input 2:</label>
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

				<label htmlFor="input3">Input 3:</label>
				<input type="text" id="input3" />

				<label htmlFor="input4">Input 4:</label>
				<input type="text" id="input4" />

				<label htmlFor="input5">Input 5:</label>
				<input type="text" id="input5" />
			</form>
		</div>
	);
}

export default App;
