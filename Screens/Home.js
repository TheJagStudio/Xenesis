import React, { useState, useEffect } from "react";
import { Text, View, Image, TouchableOpacity, ScrollView, SafeAreaView } from "react-native";
import { LinearGradient as LG } from "expo-linear-gradient";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path, Rect } from "react-native-svg";
import axios from "axios";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);
const StyledLinearGradient = styled(LG);

function Home({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [avatarId, setAvatarId] = useState();
	const [name, setName] = useState();
	const [department, setDepartment] = useState([]);
	const [event, setEvent] = useState([]);
	const [color, setColor] = useState(["bg-blue-500", "bg-red-500", "bg-orange-500", "bg-yellow-500", "bg-green-500", "bg-purple-500", "bg-blue-500", "bg-red-500", "bg-orange-500", "bg-yellow-500", "bg-green-500", "bg-purple-500"]);
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
	getData("name", setName);
	getData("profilePic", setAvatarId);
	getData("server", setServer);
	const departmentFetcher = async () => {
		axios
			.get(server + "/api/app/departmentFetcher")
			.then(function (response) {
				let data = response.data;
				setDepartment(data["data"]);
				setStatus("loaded");
			})
			.catch(function (error) {
				console.log(error);
			});
		axios
			.get(server + "/api/app/eventsListApp")
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
		departmentFetcher();
		return (
			<StyledView className="absolute top-0 left-0 z-50 w-full h-full">
				<Svg xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink" style={{ margin: "auto", background: "rgba(241, 242, 243, 0)", display: "block" }} width="201px" height="201px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
					<Rect fill="#351f62" x={5.5} y={5.5} width={42} height={42} rx={41} ry={41}></Rect>
					<Rect fill="#592cb1" x={5.5} y={5.5} width={42} height={42} rx={41} ry={41}></Rect>
					<Rect fill="#9851e4" x={5.5} y={5.5} width={42} height={42} rx={41} ry={41}></Rect>
				</Svg>
			</StyledView>
		);
	}
	return (
		<StyledLinearGradient colors={colorScheme === "dark" ? ["#351f62", "#221144", "#221144"] : ["#FFFFFF", "#FFFFFF", "#e3c9ff"]} className="bg-white dark:bg-[#221144] h-full" style={{ paddingTop: 40 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="flex flex-row p-3 bg-white dark:bg-[#221144] z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledView className="w-16 h-16 rounded-full overflow-hidden bg-slate-300 dark:bg-slate-100">
					<Image className="w-full h-full" source={{ uri: "https://storage.fleek.zone/4fd5a424-208b-4a62-a92c-49af4b184f6a-bucket/Avatars/" + avatarId + ".png" }} />
				</StyledView>
				<StyledView className="flex flex-col ml-3 mt-3">
					<StyledText className="text-[#221144]/75 dark:text-white/75">Hi there,</StyledText>
					<StyledText className="text-[#221144] dark:text-white text-xl font-bold">{name}</StyledText>
				</StyledView>
				<StyledView className="bg-white dark:bg-[#221144] absolute top-0 h-96 -translate-y-96 w-screen origin-top"></StyledView>
			</StyledView>
			<ScrollView showsHorizontalScrollIndicator={false} className="overflow-visible" stickyHeaderIndices={2}>
				<StyledText className="font-bold text-xl ml-3 mt-3 text-[#221144] dark:text-white">Departments</StyledText>
				<StyledView>
					<ScrollView horizontal={true} showsHorizontalScrollIndicator={false} className="p-3 gap-2 pr-5">
						{department.map((item, index) => (
							<StyledView key={index} className={"h-32 w-32 " + color[index] + " rounded-xl overflow-hidden shadow-lg"} style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
								<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }} source={require("../assets/loading1.png")}></Image>
								<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">{item}</StyledText>
							</StyledView>
						))}
						<StyledView className="w-3 h-full"></StyledView>
					</ScrollView>
				</StyledView>
				<StyledView className="flex flex-row justify-between">
					<StyledText className="font-bold text-xl mx-3 mt-3 text-[#221144] dark:text-white">Upcoming Events</StyledText>
					<StyledText className="font-bold text-xl mx-3 mt-3 text-[#221144]/50 dark:text-white/50">See All </StyledText>
				</StyledView>
				<StyledView>
					<ScrollView horizontal={true} showsHorizontalScrollIndicator={false} className="p-3 gap-2">
						{event.map((item, index) => (
							<StyledTouchableOpacity key={index} onPress={()=>{navigation.navigate("EventDetails",{"event":item[0]})}}>
								<StyledView className="w-64 h-fit">
									<StyledView className="h-32 w-64 bg-blue-500 rounded-xl overflow-hidden">
										<Image resizeMode="cover" className="h-full w-full" source={{ uri: server + item[4] }}></Image>
									</StyledView>
									<StyledView className="flex flex-row justify-between mt-2 px-2 items-center">
										<StyledText className="text-[#221144] dark:text-white text-lg font-bold w-screen">{item[0]}</StyledText>
									</StyledView>
									<StyledView className="flex flex-row justify-between w-full px-2">
										<StyledView>
											<StyledView className="flex flex-row items-center ">
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
											<StyledText className="text-xl font-extrabold text-[#221144] dark:text-white">₹60</StyledText>
										</StyledView>
									</StyledView>
								</StyledView>
							</StyledTouchableOpacity>
						))}
						<StyledView className="w-3 h-full"></StyledView>
					</ScrollView>
				</StyledView>
				<StyledView className="flex flex-row justify-between">
					<StyledText className="font-bold text-xl mx-3 mt-3 text-[#221144] dark:text-white">Gallary</StyledText>
					<StyledText className="font-bold text-xl mx-3 mt-3 text-[#221144]/50 dark:text-white/50">See All </StyledText>
				</StyledView>
				<StyledView className="flex flex-row justify-between gap-2 p-3 pb-0">
					<Image className="h-[30vw] w-[30vw] rounded-xl" source={{ uri: "https://source.unsplash.com/featured/300x300" }}></Image>
					<Image className="h-[30vw] w-[30vw] rounded-xl" source={{ uri: "https://source.unsplash.com/featured/300x300" }}></Image>
					<Image className="h-[30vw] w-[30vw] rounded-xl" source={{ uri: "https://source.unsplash.com/featured/300x300" }}></Image>
				</StyledView>
				<StyledView className="flex flex-row justify-between gap-2 p-3 pb-5">
					<Image className="h-[30vw] w-[30vw] rounded-xl" source={{ uri: "https://source.unsplash.com/featured/300x300" }}></Image>
					<Image className="h-[30vw] w-[30vw] rounded-xl" source={{ uri: "https://source.unsplash.com/featured/300x300" }}></Image>
					<Image className="h-[30vw] w-[30vw] rounded-xl" source={{ uri: "https://source.unsplash.com/featured/300x300" }}></Image>
				</StyledView>
			</ScrollView>
			<StyledLinearGradient colors={colorScheme === "dark" ? ["#351f62", "#221144", "#221144"] : ["#FFFFFF", "#FFFFFF", "#FFFFFF"]} className="flex flex-row justify-between p-3 pt-4 pb-6 bg-[#e3c9ff] dark:bg-[#221144] z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledView className="flex flex-col items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M6.5 14.5v-3.505c0-.245.25-.495.5-.495h2c.25 0 .5.25.5.5v3.5a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4a.5.5 0 0 0 .5-.5Z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Home</StyledText>
				</StyledView>
				<StyledTouchableOpacity
					onPress={() => {
						navigation.navigate("Explore");
					}}
					className="flex flex-col items-center"
				>
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M8 16.016a7.5 7.5 0 0 0 1.962-14.74A1 1 0 0 0 9 0H7a1 1 0 0 0-.962 1.276A7.5 7.5 0 0 0 8 16.016zm6.5-7.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z" />
						<Path d="m6.94 7.44 4.95-2.83-2.83 4.95-4.949 2.83 2.828-4.95z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Explore</StyledText>
				</StyledTouchableOpacity>
				<StyledTouchableOpacity
					onPress={() => {
						navigation.navigate("Favorites");
					}}
					className="flex flex-col items-center"
				>
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Favorites</StyledText>
				</StyledTouchableOpacity>
				<StyledTouchableOpacity
					onPress={() => {
						navigation.navigate("Tickets");
					}}
					className="flex flex-col items-center"
				>
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M4 4.85v.9h1v-.9H4Zm7 0v.9h1v-.9h-1Zm-7 1.8v.9h1v-.9H4Zm7 0v.9h1v-.9h-1Zm-7 1.8v.9h1v-.9H4Zm7 0v.9h1v-.9h-1Zm-7 1.8v.9h1v-.9H4Zm7 0v.9h1v-.9h-1Z" />
						<Path d="M1.5 3A1.5 1.5 0 0 0 0 4.5V6a.5.5 0 0 0 .5.5 1.5 1.5 0 1 1 0 3 .5.5 0 0 0-.5.5v1.5A1.5 1.5 0 0 0 1.5 13h13a1.5 1.5 0 0 0 1.5-1.5V10a.5.5 0 0 0-.5-.5 1.5 1.5 0 0 1 0-3A.5.5 0 0 0 16 6V4.5A1.5 1.5 0 0 0 14.5 3h-13ZM1 4.5a.5.5 0 0 1 .5-.5h13a.5.5 0 0 1 .5.5v1.05a2.5 2.5 0 0 0 0 4.9v1.05a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5v-1.05a2.5 2.5 0 0 0 0-4.9V4.5Z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Tickets</StyledText>
				</StyledTouchableOpacity>
				<StyledTouchableOpacity
					onPress={() => {
						navigation.navigate("Profile");
					}}
					className="flex flex-col items-center"
				>
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Profile</StyledText>
				</StyledTouchableOpacity>
			</StyledLinearGradient>
		</StyledLinearGradient>
	);
}

export default Home;
