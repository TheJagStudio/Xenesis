import React, { useState, useEffect } from "react";
import { Keyboard, Text, View, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path } from "react-native-svg";
import axios from "axios";
import MapView, { Marker } from "react-native-maps";
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
	const saveData = async (key, value) => {
		try {
			await AsyncStorage.setItem(key, value);
		} catch (error) {
			console.error(error);
		}
	};

	const getData = async (key, valueSetter) => {
		try {
			const value = await AsyncStorage.getItem(key);
			valueSetter(value);
		} catch (error) {
			console.error(error);
		}
	};
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

	const submit = async () => {
		saveData("location", location["coords"]["latitude"].toString() + "," + location["coords"]["longitude"].toString());
		navigation.navigate("Home");
	};

	const locUpdater = (newText) => {
		setQuery(newText);
		axios
			.get(url)
			.then((response) => {
				setTimeout(() => {
					let tempData = response.data;
					let dataArr = tempData["features"];
					let finalArr = [];
					for (let i = 0; i < dataArr.length; i++) {
						const element = dataArr[i];
						finalArr.push({
							name: element["place_name"],
							Lat: element["center"][1],
							Lon: element["center"][0],
						});
					}
					setSearchList(finalArr);
					setShowSearchList(true);
				}, 2000);
			})
			.catch((error) => {
				console.log(error);
			});
	};
	const url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + query + ".json?limit=5&language=en-US&access_token=pk.eyJ1IjoiZGV2cGF0ZWwzMjciLCJhIjoiY2xkdmxpcW5tMGgzOTNwcG5qMWFvbzZrMCJ9.P3EXduadE-bAqd0nkBNGkQ";
	return (
		<SafeAreaView className="bg-white dark:bg-[#28272C] h-full" style={{ paddingTop: Platform.OS === "android" ? 40 : 0 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="p-3 bg-white dark:bg-[#28272C]  z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledTouchableOpacity onPress={() => navigation.navigate("AccountSetup")} className="w-[30px] h-[30px] items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#28272C"}`} viewBox="0 0 16 16">
						<Path fillRule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
					</Svg>
				</StyledTouchableOpacity>
				<StyledView className="bg-white dark:bg-[#28272C] absolute top-0 h-96 -translate-y-96 w-screen origin-top"></StyledView>
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
						<TextInput
							onChangeText={(newText) => {
								locUpdater(newText);
							}}
							onChange={(newText) => {
								locUpdater(newText);
							}}
							className="text-black dark:text-white w-[80%]"
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Search Your Location"
							value={query}
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
						<StyledTouchableOpacity className="items-center">
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
										Keyboard.dismiss();
										setQuery("");
									}}
									className={"py-2 " + `${searchList.length - 1 == index ? "border-b-0" : "border-b-2"}` + " border-white w-full px-4"}
								>
									<StyledText className="text-gray-500 dark:text-white text-md font-bold">{locArr.name}</StyledText>
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
							latitudeDelta: 0.05,
							longitudeDelta: 0.05,
						}}
						onRegionChange={() => ({
							latitude: location["coords"]["latitude"],
							longitude: location["coords"]["longitude"],
						})}
					>
						<Marker
							coordinate={{
								latitude: location["coords"]["latitude"],
								longitude: location["coords"]["longitude"],
							}}
							title={"current"}
							description={"trial"}
						/>
					</MapView>
				</StyledView>
			</KeyboardAvoidingView>
			<StyledView className={"w-[80%] mx-[10%] mt-10 " + `${Platform.OS === "android" ? "" : "absolute bottom-10"}`}>
				<StyledTouchableOpacity className="rounded-full w-[80%] mx-[10%] bg-[#FEA500] shadow-xl mb-3" onPress={submit}>
					<StyledText className="text-center py-3 text-xl font-bold text-white ">Next</StyledText>
				</StyledTouchableOpacity>
			</StyledView>
		</SafeAreaView>
	);
}

export default ChooseLocation;
