import React, { useState, useEffect } from "react";
import { Text, View, Image, TouchableOpacity, ScrollView, SafeAreaView } from "react-native";
import { LinearGradient as LG } from "expo-linear-gradient";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path } from "react-native-svg";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);
const StyledLinearGradient = styled(LG);

function Tickets({ navigation }) {
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
			<StyledText className="text-xl text-[#221144] dark:text-white">Tickets</StyledText>
			</ScrollView>
			<StyledLinearGradient colors={colorScheme === "dark" ? ["#351f62", "#221144", "#221144"] : ["#FFFFFF", "#FFFFFF", "#FFFFFF"]} className="flex flex-row justify-between p-3 pt-4 pb-6 bg-[#e3c9ff] dark:bg-[#221144] z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledTouchableOpacity onPress={() => {
						navigation.navigate("Home");
					}} 
					className="flex flex-col items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4.5a.5.5 0 0 0 .5-.5v-4h2v4a.5.5 0 0 0 .5.5H14a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146ZM2.5 14V7.707l5.5-5.5 5.5 5.5V14H10v-4a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v4H2.5Z"/>
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Home</StyledText>
				</StyledTouchableOpacity>
				<StyledTouchableOpacity 
					onPress={() => {
						navigation.navigate("Explore");
					}}
					className="flex flex-col items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M8 16.016a7.5 7.5 0 0 0 1.962-14.74A1 1 0 0 0 9 0H7a1 1 0 0 0-.962 1.276A7.5 7.5 0 0 0 8 16.016zm6.5-7.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z" />
						<Path d="m6.94 7.44 4.95-2.83-2.83 4.95-4.949 2.83 2.828-4.95z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Explore</StyledText>
				</StyledTouchableOpacity>
				<StyledView
					onPress={() => {
						navigation.navigate("Favorites");
					}}
					className="flex flex-col items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
					<Path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Favorites</StyledText>
				</StyledView>
				<StyledView className="flex flex-col items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={28} height={28} fill={`${colorScheme === "dark" ? "white" : "#221144"}`} className="bi bi-house-door-fill" viewBox="0 0 16 16">
						<Path d="M0 4.5A1.5 1.5 0 0 1 1.5 3h13A1.5 1.5 0 0 1 16 4.5V6a.5.5 0 0 1-.5.5 1.5 1.5 0 0 0 0 3 .5.5 0 0 1 .5.5v1.5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 11.5V10a.5.5 0 0 1 .5-.5 1.5 1.5 0 1 0 0-3A.5.5 0 0 1 0 6V4.5Zm4-1v1h1v-1H4Zm1 3v-1H4v1h1Zm7 0v-1h-1v1h1Zm-1-2h1v-1h-1v1Zm-6 3H4v1h1v-1Zm7 1v-1h-1v1h1Zm-7 1H4v1h1v-1Zm7 1v-1h-1v1h1Zm-8 1v1h1v-1H4Zm7 1h1v-1h-1v1Z" />
					</Svg>
					<StyledText className="text-[#221144] dark:text-white text-md font-semibold">Tickets</StyledText>
				</StyledView>
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

export default Tickets;
