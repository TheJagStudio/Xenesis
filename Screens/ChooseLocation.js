import React, { useState, useEffect } from "react";
import { Keyboard, Text, View, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView } from "react-native";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path } from "react-native-svg";
import axios from "axios";
import MapView from "react-native-maps";
import * as Location from "expo-location";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);

function ChooseLocation({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [query, setQuery] = useState("");
	const [searchList, setSearchList] = useState([]);
	const [showSearchList, setShowSearchList] = useState(false);
	const [location, setLocation] = useState({
		coords: {
			accuracy: 5,
			altitude: 5,
			altitudeAccuracy: 0.5,
			heading: 0,
			latitude: 23.2124,
			longitude: 72.627,
			speed: 0,
		},
		mocked: false,
		timestamp: 1675267904454,
	});
	const [errorMsg, setErrorMsg] = useState(null);
	useEffect(() => {
		(async () => {
			let { status } = await Location.requestForegroundPermissionsAsync();
			if (status !== "granted") {
				setErrorMsg("Permission to access location was denied");
				return;
			}

			let location = await Location.getCurrentPositionAsync({});
			setLocation(location);
		})();
	}, []);

	const url = "https://www.openstreetmap.org/geocoder/search_osm_nominatim?query=" + query;
	// <ul class='results-list list-group list-group-flush'>
	//   <li class="list-group-item search_results_entry">City <a class="set_position" data-lat="23.2232877" data-lon="72.6492267" data-min-lat="23.1649739" data-max-lat="23.2770054" data-min-lon="72.6025742" data-max-lon="72.6890629" data-prefix="City" data-name="Gandhinagar, Gandhinagar Taluka, Gandhinagar District, Gujarat, India" data-type="way" data-id="1104668864" href="/way/1104668864">Gandhinagar, Gandhinagar Taluka, Gandhinagar District, Gujarat, India</a></li>
	//   <li class="list-group-item search_results_entry">Village <a class="set_position" data-lat="17.1783774" data-lon="79.6064446" data-min-lat="17.1583774" data-max-lat="17.1983774" data-min-lon="79.5864446" data-max-lon="79.6264446" data-prefix="Village" data-name="Gandhinagar, Suryapet mandal, Suryapet, Telangana, 508376, India" data-type="node" data-id="6655178019" href="/node/6655178019">Gandhinagar, Suryapet mandal, Suryapet, Telangana, 508376, India</a></li>
	//   <li class="list-group-item search_results_entry">Suburb <a class="set_position" data-lat="12.3226718" data-lon="76.6649751" data-min-lat="12.3026718" data-max-lat="12.3426718" data-min-lon="76.6449751" data-max-lon="76.6849751" data-prefix="Suburb" data-name="Gandhinagar, Mysuru, Mysuru taluk, Mysuru district, Karnataka, 570001, India" data-type="node" data-id="1001763025" href="/node/1001763025">Gandhinagar, Mysuru, Mysuru taluk, Mysuru district, Karnataka, 570001, India</a></li>
	//   <li class="list-group-item search_results_entry">Suburb <a class="set_position" data-lat="15.4347553" data-lon="75.0183502" data-min-lat="15.4147553" data-max-lat="15.4547553" data-min-lon="74.9983502" data-max-lon="75.0383502" data-prefix="Suburb" data-name="Gandhinagar, Dharwad, Dharawada taluku, Dharwad district, Karnataka, 580001, India" data-type="node" data-id="4072713547" href="/node/4072713547">Gandhinagar, Dharwad, Dharawada taluku, Dharwad district, Karnataka, 580001, India</a></li>
	//   <li class="list-group-item search_results_entry">Suburb <a class="set_position" data-lat="12.9254215" data-lon="74.8541336" data-min-lat="12.9054215" data-max-lat="12.9454215" data-min-lon="74.8341336" data-max-lon="74.8741336" data-prefix="Suburb" data-name="Gandhinagar, Kavoor, Mangaluru taluk, Dakshina Kannada district, Karnataka, 575015, India" data-type="node" data-id="3263831336" href="/node/3263831336">Gandhinagar, Kavoor, Mangaluru taluk, Dakshina Kannada district, Karnataka, 575015, India</a></li>
	//   <li class="list-group-item search_results_entry">Village <a class="set_position" data-lat="10.9539939" data-lon="78.5661749" data-min-lat="10.9339939" data-max-lat="10.9739939" data-min-lon="78.5461749" data-max-lon="78.5861749" data-prefix="Village" data-name="Gandhinagar, Musiri, Tiruchirappalli District, Tamil Nadu, 621006, India" data-type="node" data-id="9864398334" href="/node/9864398334">Gandhinagar, Musiri, Tiruchirappalli District, Tamil Nadu, 621006, India</a></li>
	//   <li class="list-group-item search_results_entry">Village <a class="set_position" data-lat="11.0902287" data-lon="78.6747694" data-min-lat="11.0702287" data-max-lat="11.1102287" data-min-lon="78.6547694" data-max-lon="78.6947694" data-prefix="Village" data-name="Gandhinagar, Musiri, Tiruchirappalli District, Tamil Nadu, 621004, India" data-type="node" data-id="9671919176" href="/node/9671919176">Gandhinagar, Musiri, Tiruchirappalli District, Tamil Nadu, 621004, India</a></li>
	//   <li class="list-group-item search_results_entry">Village <a class="set_position" data-lat="10.7148555" data-lon="78.6173058" data-min-lat="10.6948555" data-max-lat="10.7348555" data-min-lon="78.5973058" data-max-lon="78.6373058" data-prefix="Vi      <div class="text-center loader">
	return (
		<SafeAreaView className="bg-white dark:bg-[#28272C] h-full" style={{ paddingTop: Platform.OS === "android" ? 40 : 0 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-6 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="p-3">
				<StyledTouchableOpacity onPress={() => navigation.navigate("AccountSetup")} className="w-[30px] h-[30px] items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#28272C"}`} viewBox="0 0 16 16">
						<Path fillRule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
					</Svg>
				</StyledTouchableOpacity>
			</StyledView>
			<KeyboardAvoidingView behavior="position">
				<StyledView className="p-5">
					<StyledText className="text-[#28272C] dark:text-white text-4xl font-bold">Choose</StyledText>
					<StyledText className="text-[#28272C] dark:text-white text-4xl font-bold">Your Location</StyledText>
					<StyledText className="text-gray-500 dark:text-gray-300 text-md mt-3">Uncover the hottest event in your location. Choose your loaction below to get started.</StyledText>
				</StyledView>
				<StyledView className="w-[90%] mx-auto mt-3">
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z" />
							<Path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[80%]" onChangeText={(newText) => setQuery(newText)} onSubmitEditing={Keyboard.dismiss} placeholder="Search Your Location" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
						<StyledTouchableOpacity
							onPress={() => {
								axios
									.get(url)
									.then((response) => {
										setTimeout(() => {
											let tempData = response.data;
											let dataArr = tempData.split("<li");
											let finalArr = [];
											for (let i = 1; i < 5; i++) {
												try {
													const type = dataArr[i].split(">")[1].split("<")[0];
													const Lat = dataArr[i].split("data-lat=")[1].split(" ")[0].replace(/"/g, "");
													const Lon = dataArr[i].split("data-lon=")[1].split(" ")[0].replace(/"/g, "");
													const minLat = dataArr[i].split("data-min-lat=")[1].split(" ")[0].replace(/"/g, "");
													const MaxLat = dataArr[i].split("data-max-lat=")[1].split(" ")[0].replace(/"/g, "");
													const MinLon = dataArr[i].split("data-min-lon=")[1].split(" ")[0].replace(/"/g, "");
													const name = dataArr[i].split("data-name=")[1].split('"')[1].replace(/"/g, "");
													finalArr.push({
														type: type,
														Lat: Lat,
														Lon: Lon,
														minLat: minLat,
														MaxLat: MaxLat,
														MinLon: MinLon,
														name: name,
													});
												} catch (e) {}
											}
											setSearchList(finalArr);
											setShowSearchList(true);
											Keyboard.dismiss();
										}, 2000);
									})
									.catch((error) => {
										console.log(error);
									});
							}}
							className="items-center"
						>
							<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="scale-75" viewBox="0 0 16 16">
								<Path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
							</Svg>
						</StyledTouchableOpacity>
					</StyledView>
					<StyledView className={`${showSearchList === true ? "block" : "hidden"}` + " bg-slate-300/50 dark:bg-slate-700/50 shadow-lg rounded-lg "}>
						{searchList.map((locArr, index) => {
							return (
								<StyledTouchableOpacity
									key={index}
									onPress={() => {
										setShowSearchList(false);
										setLocation({
											coords: {
												accuracy: location["coords"]["accuracy"],
												altitude: location["coords"]["altitude"],
												altitudeAccuracy: location["coords"]["altitudeAccuracy"],
												heading: location["coords"]["heading"],
												latitude: locArr.Lat,
												longitude: locArr.Lon,
												speed: location["coords"]["speed"],
											},
											mocked: location["mocked"],
											timestamp: location["timestamp"],
										});
									}}
									className={"py-2 " + `${searchList.length - 1 == index ? "border-b-0" : "border-b-2"}` + " border-white w-full px-4"}
								>
									<StyledText className="text-gray-500 dark:text-white text-md font-bold">
										{locArr.type} : {locArr.name}
									</StyledText>
								</StyledTouchableOpacity>
							);
						})}
					</StyledView>
				</StyledView>
				<StyledView className="w-[90%] h-64 mx-auto rounded-lg overflow-hidden mt-3">
					<MapView
						className="w-full h-full"
						region={{
							latitude: location["coords"]["latitude"],
							longitude: location["coords"]["longitude"],
							latitudeDelta: 0.0422,
							longitudeDelta: 0.0421,
						}}
						onRegionChange={{
							latitude: location["coords"]["latitude"],
							longitude: location["coords"]["longitude"],
							latitudeDelta: 0.0422,
							longitudeDelta: 0.0421,
						}}
					/>
				</StyledView>
			</KeyboardAvoidingView>
			<StyledView className="w-[80%] mx-[10%] mt-10 absolute bottom-10">
				<StyledTouchableOpacity className="rounded-full w-[80%] mx-[10%] bg-[#FEA500] shadow-xl mb-3" onPress={() => navigation.navigate("ChooseLocation")}>
					<StyledText className="text-center py-3 text-xl font-bold text-white ">Next</StyledText>
				</StyledTouchableOpacity>
			</StyledView>
		</SafeAreaView>
	);
}

export default ChooseLocation;
