import React, { useState, useEffect } from "react";
import { Text, View, Image, TouchableOpacity, ScrollView, SafeAreaView } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path } from "react-native-svg";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);

function ChooseLocation({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [avatarId, setAvatarId] = useState();
	const [name, setName] = useState();
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

	return (
		<SafeAreaView className="bg-white dark:bg-[#28272C] h-full" style={{ paddingTop: Platform.OS === "android" ? 40 : 0 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="flex flex-row p-3 bg-white dark:bg-[#28272C] z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledView className="w-16 h-16 rounded-full overflow-hidden bg-slate-300 dark:bg-slate-100">
					<Image className="w-full h-full" source={{ uri: "https://storage.fleek.zone/4fd5a424-208b-4a62-a92c-49af4b184f6a-bucket/Avatars/" + avatarId + ".png" }} />
				</StyledView>
				<StyledView className="flex flex-col ml-3 mt-3">
					<StyledText className="text-black/75 dark:text-white/75">Hi there,</StyledText>
					<StyledText className="text-black dark:text-white text-xl font-bold">{name}</StyledText>
				</StyledView>
				<StyledView className="bg-white dark:bg-[#28272C] absolute top-0 h-96 -translate-y-96 w-screen origin-top"></StyledView>
			</StyledView>
			<StyledText className="font-bold text-xl ml-3 mt-3 text-black dark:text-white">Categories</StyledText>
			<StyledView>
				<ScrollView horizontal={true} showsHorizontalScrollIndicator={false} className="p-3 gap-2 pr-5">
					<StyledView className="h-32 w-32 bg-blue-500 rounded-xl overflow-hidden" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }}>
						<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} source={require("../assets/loading1.png")}></Image>
						<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">Event 1</StyledText>
					</StyledView>
					<StyledView className="h-32 w-32 bg-red-500 rounded-xl overflow-hidden" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }}>
						<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} source={require("../assets/loading2.png")}></Image>
						<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">Event 2</StyledText>
					</StyledView>
					<StyledView className="h-32 w-32 bg-orange-500 rounded-xl overflow-hidden" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }}>
						<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} source={require("../assets/loading3.png")}></Image>
						<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">Event 3</StyledText>
					</StyledView>
					<StyledView className="h-32 w-32 bg-yellow-500 rounded-xl overflow-hidden" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }}>
						<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} source={require("../assets/loading1.png")}></Image>
						<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">Event 4</StyledText>
					</StyledView>
					<StyledView className="h-32 w-32 bg-green-500 rounded-xl overflow-hidden" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }}>
						<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} source={require("../assets/loading2.png")}></Image>
						<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">Event 5</StyledText>
					</StyledView>
					<StyledView className="h-32 w-32 bg-purple-500 rounded-xl overflow-hidden" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }}>
						<Image resizeMode="contain" className="absolute top-0 -right-2  w-[75%] h-[75%] scale-125" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} source={require("../assets/loading3.png")}></Image>
						<StyledText className="text-white text-lg font-bold m-3 absolute bottom-0">Event 6</StyledText>
					</StyledView>
					<StyledView className="w-3 h-full"></StyledView>
				</ScrollView>
			</StyledView>
			<StyledView className="flex flex-row justify-between">
				<StyledText className="font-bold text-xl mx-3 mt-3 text-black dark:text-white">Upcoming Events</StyledText>
				<StyledText className="font-bold text-xl mx-3 mt-3 text-black/50 dark:text-white/50">See All </StyledText>
			</StyledView>
			<StyledView>
				<ScrollView horizontal={true} showsHorizontalScrollIndicator={false} className="p-3 gap-2">
					<StyledView className="w-64 h-fit">
						<StyledView className="h-32 w-64 bg-blue-500 rounded-xl overflow-hidden">
							<Image resizeMode="cover" className="h-full w-full" source={require("../assets/event1.jpg")}></Image>
						</StyledView>
						<StyledView className="flex flex-row justify-between mt-2 px-2 items-center">
							<StyledText className="text-black dark:text-white text-lg  font-bold w-[80%]">Event 1</StyledText>
							<Svg xmlns="http://www.w3.org/2000/svg" width={20} height={20} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="" viewBox="0 0 16 16">
								<Path d="M5.5 4a.5.5 0 0 0-.5.5v5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 .5-.5v-5a.5.5 0 0 0-.5-.5h-5zm1 7a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1h-3z" />
								<Path d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-1h1v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1H1V2a2 2 0 0 1 2-2z" />
								<Path d="M1 5v-.5a.5.5 0 0 1 1 0V5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0V8h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0v.5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1z" />
							</Svg>
						</StyledView>
						<StyledView className="flex flex-row justify-between w-full px-2">
							<StyledView>
								<StyledView className="flex flex-row items-center ">
									<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
										<Path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z" />
										<Path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
									</Svg>
									<StyledText className="text-black dark:text-white">Lab E7</StyledText>
								</StyledView>
								<StyledView className="flex flex-row items-center ">
									<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
										<Path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
									</Svg>
									<StyledText className="text-black dark:text-white">14 / 15 March</StyledText>
								</StyledView>
							</StyledView>
							<StyledView className="flex flex-col items-center">
								<StyledText className="text-black dark:text-white">Starts at</StyledText>
								<StyledText className="text-xl font-extrabold text-black dark:text-white">₹60</StyledText>
							</StyledView>
						</StyledView>
					</StyledView>
					<StyledView className="w-64 h-fit">
						<StyledView className="h-32 w-64 bg-blue-500 rounded-xl overflow-hidden">
							<Image resizeMode="cover" className="h-full w-full" source={require("../assets/event2.jpg")}></Image>
						</StyledView>
						<StyledView className="flex flex-row justify-between mt-2 px-2 items-center">
							<StyledText className="text-black dark:text-white text-lg  font-bold w-[80%]">Event 2</StyledText>
							<Svg xmlns="http://www.w3.org/2000/svg" width={20} height={20} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="" viewBox="0 0 16 16">
								<Path d="M5.5 4a.5.5 0 0 0-.5.5v5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 .5-.5v-5a.5.5 0 0 0-.5-.5h-5zm1 7a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1h-3z" />
								<Path d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-1h1v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1H1V2a2 2 0 0 1 2-2z" />
								<Path d="M1 5v-.5a.5.5 0 0 1 1 0V5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0V8h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0v.5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1z" />
							</Svg>
						</StyledView>
						<StyledView className="flex flex-row justify-between w-full px-2">
							<StyledView>
								<StyledView className="flex flex-row items-center ">
									<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
										<Path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z" />
										<Path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
									</Svg>
									<StyledText className="text-black dark:text-white">Lab F5</StyledText>
								</StyledView>
								<StyledView className="flex flex-row items-center ">
									<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
										<Path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
									</Svg>
									<StyledText className="text-black dark:text-white">14 / 15 March</StyledText>
								</StyledView>
							</StyledView>
							<StyledView className="flex flex-col items-center">
								<StyledText className="text-black dark:text-white">Starts at</StyledText>
								<StyledText className="text-xl font-extrabold text-black dark:text-white">₹50</StyledText>
							</StyledView>
						</StyledView>
					</StyledView>
					<StyledView className="w-64 h-fit">
						<StyledView className="h-32 w-64 bg-blue-500 rounded-xl overflow-hidden">
							<Image resizeMode="cover" className="h-full w-full" source={require("../assets/event3.jpg")}></Image>
						</StyledView>
						<StyledView className="flex flex-row justify-between mt-2 px-2 items-center">
							<StyledText className="text-black dark:text-white text-lg  font-bold w-[80%]">Event 3</StyledText>
							<Svg xmlns="http://www.w3.org/2000/svg" width={20} height={20} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="" viewBox="0 0 16 16">
								<Path d="M5.5 4a.5.5 0 0 0-.5.5v5a.5.5 0 0 0 .5.5h5a.5.5 0 0 0 .5-.5v-5a.5.5 0 0 0-.5-.5h-5zm1 7a.5.5 0 0 0 0 1h3a.5.5 0 0 0 0-1h-3z" />
								<Path d="M3 0h10a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-1h1v1a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1H1V2a2 2 0 0 1 2-2z" />
								<Path d="M1 5v-.5a.5.5 0 0 1 1 0V5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0V8h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1zm0 3v-.5a.5.5 0 0 1 1 0v.5h.5a.5.5 0 0 1 0 1h-2a.5.5 0 0 1 0-1H1z" />
							</Svg>
						</StyledView>
						<StyledView className="flex flex-row justify-between w-full px-2">
							<StyledView>
								<StyledView className="flex flex-row items-center ">
									<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
										<Path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A31.493 31.493 0 0 1 8 14.58a31.481 31.481 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z" />
										<Path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />
									</Svg>
									<StyledText className="text-black dark:text-white">Lab A2</StyledText>
								</StyledView>
								<StyledView className="flex flex-row items-center ">
									<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-2 scale-75" viewBox="0 0 16 16">
										<Path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
									</Svg>
									<StyledText className="text-black dark:text-white">14 / 15 March</StyledText>
								</StyledView>
							</StyledView>
							<StyledView className="flex flex-col items-center">
								<StyledText className="text-black dark:text-white">Starts at</StyledText>
								<StyledText className="text-xl font-extrabold text-black dark:text-white">₹90</StyledText>
							</StyledView>
						</StyledView>
					</StyledView>
					<StyledView className="w-3 h-full"></StyledView>
				</ScrollView>
			</StyledView>
		</SafeAreaView>
	);
}

export default ChooseLocation;
