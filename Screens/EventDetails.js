import React, { useState } from "react";
import { Text, View, TouchableOpacity, ScrollView, Image } from "react-native";
import { styled, useColorScheme } from "nativewind";
import { LinearGradient as LG } from "expo-linear-gradient";
import AsyncStorage from "@react-native-async-storage/async-storage";
import Swiper from "react-native-swiper";
import Svg, { Circle, Rect, Mask, G, Path, Defs, LinearGradient, Stop } from "react-native-svg";
import axios from "axios";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);
const StyledLinearGradient = styled(LG);
function EventDetails({ navigation: { goBack }, route }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [event, setEvent] = useState([]);
	const [server, setServer] = useState("");
	const [status, setStatus] = useState("loading");
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
	getData("server", setServer);
	const eventFetcher = async () => {
		var data = JSON.stringify({
			event: route.params.event,
		});

		var config = {
			method: "post",
			maxBodyLength: Infinity,
			url: server + "/api/app/eventDetailFetcher",
			headers: {
				"Content-Type": "application/json",
			},
			data: data,
		};

		axios(config)
			.then(function (response) {
				let data = response.data;
				setEvent(data["data"]);
				setStatus("loaded");
			})
			.catch(function (error) {
				console.log(error);
			});
	};
	if (status === "loading") {
		eventFetcher();
		return <StyledLinearGradient colors={colorScheme === "dark" ? ["#351f62", "#221144", "#221144"] : ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#e3c9ff"]} className="h-full justify-center bg-white dark:bg-[#221144] transition-[background] duration-300"></StyledLinearGradient>;
	}
	function rules() {
		if (event[4] != []) {
			return (
				<StyledView>
					<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">Rules</StyledText>
					<StyledView className="pl-2">
						{event[4].map((item, index) => (
							<StyledText key={index} className="text-[#221144] dark:text-white px-3 text-justify py-1">
								• {item.trim()}
							</StyledText>
						))}
					</StyledView>
				</StyledView>
			);
		}
	}
	function round1() {
		if (event[5] != null) {
			return (
				<StyledView>
					<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">Round 1 : {event[5]}</StyledText>
					<StyledView className="pl-2">
						{event[6].map((item, index) => (
							<StyledText key={index} className="text-[#221144] dark:text-white px-3 text-justify py-1">
								• {item.trim()}
							</StyledText>
						))}
					</StyledView>
				</StyledView>
			);
		}
	}
	function round2() {
		if (event[7] != null) {
			return (
				<StyledView>
					<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">Round 2 : {event[7]}</StyledText>
					<StyledView className="pl-2">
						{event[8].map((item, index) => (
							<StyledText key={index} className="text-[#221144] dark:text-white px-3 text-justify py-1">
								• {item.trim()}
							</StyledText>
						))}
					</StyledView>
				</StyledView>
			);
		}
	}
	function round3() {
		if (event[9] != null) {
			return (
				<StyledView>
					<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">Round 3 : {event[9]}</StyledText>
					<StyledView className="pl-2">
						{event[10].map((item, index) => (
							<StyledText key={index} className="text-[#221144] dark:text-white px-3 text-justify py-1">
								• {item.trim()}
							</StyledText>
						))}
					</StyledView>
				</StyledView>
			);
		}
	}
	function round4() {
		if (event[11] != null) {
			return (
				<StyledView>
					<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">Round 4 : {event[11]}</StyledText>
					<StyledView className="pl-2">
						{event[12].map((item, index) => (
							<StyledText key={index} className="text-[#221144] dark:text-white px-3 text-justify py-1">
								• {item.trim()}
							</StyledText>
						))}
					</StyledView>
				</StyledView>
			);
		}
	}
	function round5() {
		if (event[13] != null) {
			return (
				<StyledView>
					<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">Round 5: {event[13]}</StyledText>
					<StyledView className="pl-2">
						{event[14].map((item, index) => (
							<StyledText key={index} className="text-[#221144] dark:text-white px-3 text-justify py-1">
								• {item.trim()}
							</StyledText>
						))}
					</StyledView>
				</StyledView>
			);
		}
	}
	return (
		<StyledLinearGradient colors={colorScheme === "dark" ? ["#351f62", "#221144", "#221144"] : ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#e3c9ff"]} className="h-full justify-center bg-white dark:bg-[#221144] transition-[background] duration-300">
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="p-3 bg-white dark:bg-[#221144]  z-40 shadow-lg pt-[40]" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledTouchableOpacity onPress={goBack} className="w-[30px] h-[30px] items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#221144"}`} viewBox="0 0 16 16">
						<Path fillRule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
					</Svg>
				</StyledTouchableOpacity>
				<StyledView className="bg-white dark:bg-[#221144] absolute top-0 h-96 -translate-y-96 w-screen origin-top"></StyledView>
			</StyledView>
			<Swiper showsButtons={false} loop={true} autoplay={true} autoplayTimeout={5} bounces={true} activeDotColor={"#211E60"} dotColor={"#FFFFFF"}>
				<Image className="w-full h-full shadow-xl" resizeMode="cover" source={require("../assets/images/events/1.jpg")}></Image>
				<Image className="w-full h-full shadow-xl" resizeMode="cover" source={require("../assets/images/events/2.jpg")}></Image>
				<Image className="w-full h-full shadow-xl" resizeMode="cover" source={require("../assets/images/events/3.jpg")}></Image>
				<Image className="w-full h-full shadow-xl" resizeMode="cover" source={require("../assets/images/events/4.jpg")}></Image>
			</Swiper>
			<ScrollView showsHorizontalScrollIndicator={false} className=" h-[40%] w-full" stickyHeaderHiddenOnScroll={false} stickyHeaderIndices={[0]}>
				<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white bg-white dark:bg-[#221144] p-3">{event[0]}</StyledText>
				<StyledView className="flex flex-row justify-between w-full mt-3 px-3">
					<StyledView>
						<StyledView className="flex flex-row items-center">
							<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
								<Path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z" />
								<Path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
							</Svg>
							<StyledText className="text-[#221144] dark:text-white">Lab E7</StyledText>
						</StyledView>
						<StyledView className="flex flex-row items-center ">
							<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
								<Path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
							</Svg>
							<StyledText className="text-[#221144] dark:text-white">14 / 15 March</StyledText>
						</StyledView>
					</StyledView>
					<StyledView className="flex flex-col items-center">
						<StyledText className="text-[#221144] dark:text-white">Starts at</StyledText>
						<StyledText className="text-xl font-extrabold text-[#221144] dark:text-white">₹{event[1]}</StyledText>
					</StyledView>
				</StyledView>
				<StyledText className="text-xl font-bold text-[#221144] capitalize dark:text-white mt-5 px-3">About This Event</StyledText>
				<StyledText className="text-[#221144] dark:text-white px-3 text-justify py-2">{event[2]}</StyledText>
				{rules()}
				{round1()}
				{round2()}
				{round3()}
				{round4()}
				{round5()}
				<StyledView className="h-32"></StyledView>
			</ScrollView>
			<StyledTouchableOpacity className="rounded-lg w-[80%] mx-[10%] bg-[#442c72] shadow-xl mb-3 absolute bottom-10">
				<StyledText className="text-center py-3 text-xl font-bold text-white ">Get a Ticket</StyledText>
			</StyledTouchableOpacity>
		</StyledLinearGradient>
	);
}

export default EventDetails;
