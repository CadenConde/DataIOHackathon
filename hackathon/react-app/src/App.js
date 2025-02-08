import React, { useState } from "react";
import "./App.css";

function App() {
	const [selectedOption, setSelectedOption] = useState("");

	const handleDropdownChange = event => {
		setSelectedOption(event.target.value);
	};
	return (
		<div className="App">
			<form>
				{/* Dropdown menu */}
				<label htmlFor="dropdown">Choose an option:</label>
				<select id="dropdown" value={selectedOption} onChange={handleDropdownChange}>
					<option value="">--Select--</option>
					<option value="option1">Option 1</option>
					<option value="option2">Option 2</option>
					<option value="option3">Option 3</option>
				</select>

				{/* Other input fields */}
				<label htmlFor="input2">Input 2:</label>
				<input type="text" id="input2" />

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
