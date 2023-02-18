import React, { useState } from "react";
import { Keyboard, Text, View, Image, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView, Platform, Alert } from "react-native";
import { LinearGradient as LG } from "expo-linear-gradient";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path } from "react-native-svg";
import axios from "axios";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);
const StyledLinearGradient = styled(LG);

function AccountSetup({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [avatarId, setAvatarId] = useState("0001");
	const [imageAnim, setImageAnim] = useState(false);
	const [imageCover, setImageCover] = useState(false);
	const [server, setServer] = useState("");
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
	const [email, setEmail] = useState("");
	getData("email", setEmail);
	getData("server", setServer);
	const [name, setName] = useState("");
	const [phone, setPhone] = useState("");
	const [college, setCollege] = useState("");
	const [buttonStatus, setButtonStatus] = useState("inactive");
	//navigation.navigate("ChooseLocation")
	const submit = async () => {
		if (name != "" && phone != "" && phone.length == 10 && college != "") {
			var data = JSON.stringify({
				email: email,
				name: name,
				phone: phone,
				college: college,
				profilePic: avatarId,
			});
			var config = {
				method: "post",
				maxBodyLength: Infinity,
				url: server + "/api/app/accountSetup",
				headers: {
					"Content-Type": "application/json",
				},
				data: data,
			};
			axios(config)
				.then(function (response) {
					let data = response.data;
					if (data.hasOwnProperty("msg")) {
						saveData("name", name);
						saveData("phone", phone);
						saveData("college", college);
						saveData("profilePic", avatarId);
						navigation.navigate("ChooseLocation");
					} else {
						Alert.alert(data["error"]);
					}
				})
				.catch(function (error) {
					return Alert.alert(error);
				});
		} else {
			if (phone.length == 10) {
				return Alert.alert("Please enter all details.");
			} else {
				return Alert.alert("Phone Number must be 10 digits");
			}
		}
	};
	return (
		<StyledLinearGradient colors={colorScheme === "dark" ? ["#351f62", "#221144", "#221144"] : ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#e3c9ff"]} className="bg-white dark:bg-[#221144] h-full" style={{ paddingTop: 40 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="p-3 bg-white dark:bg-[#221144]  z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledTouchableOpacity onPress={() => navigation.navigate("LoginEmail")} className="w-[30px] h-[30px] items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#221144"}`} viewBox="0 0 16 16">
						<Path fillRule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
					</Svg>
				</StyledTouchableOpacity>
				<StyledView className="bg-white dark:bg-[#221144] absolute top-0 h-96 -translate-y-96 w-screen origin-top"></StyledView>
			</StyledView>
			<KeyboardAvoidingView behavior="position">
				<StyledTouchableOpacity
					className="mx-auto mb-5 mt-5 h-32 w-32 bg-[#e3c9ff] dark:bg-[#442c72] rounded-full overflow-hidden"
					onPress={() => {
						let tempId = (parseInt(avatarId) + 1) % 100;
						if (tempId == 0) {
							tempId = 1;
						}
						if (tempId.toString().length == 1) {
							tempId = "000" + tempId.toString();
						} else {
							tempId = "00" + tempId.toString();
						}
						setAvatarId(tempId);
						setImageAnim(true);
						setImageCover(true);
						setTimeout(function () {
							setImageAnim(false);
						}, 400);
					}}
				>
					<Image className="translate-y-0 focus:translate-y-32 transition-all duration-300 w-full h-full" style={{ shadowColor: colorScheme === "dark" ? "#FFFFFF" : "#000000", shadowOpacity: 0.7, shadowRadius: 20 }} resizeMode="contain" source={{ uri: "https://storage.fleek.zone/4fd5a424-208b-4a62-a92c-49af4b184f6a-bucket/Avatars/" + avatarId + ".png" }} />
					<Svg className={`${imageCover === true ? "hidden" : ""}` + "absolute top-0 left-0 bg-slate-900/50"} xmlns="http://www.w3.org/2000/svg" width={130} height={130} fill="#FFFFFF" viewBox="-12 -12 40 40">
						<Path d="M15 12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h1.172a3 3 0 0 0 2.12-.879l.83-.828A1 1 0 0 1 6.827 3h2.344a1 1 0 0 1 .707.293l.828.828A3 3 0 0 0 12.828 5H14a1 1 0 0 1 1 1v6zM2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2z" />
						<Path d="M8 11a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5zm0 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM3 6.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z" />
					</Svg>
				</StyledTouchableOpacity>
				<StyledView className="w-[90%] mx-auto mt-3">
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3" viewBox="0 0 16 16">
							<Path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z" />
						</Svg>
						<TextInput
							value={name}
							onChangeText={(name) => {
								setName(name);
								if (name != "" && college != "" && phone != "" && phone.length == 10) {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							className="text-black dark:text-white w-[85%]"
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Full Name"
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
						</Svg>
						<TextInput
							value={college}
							onChangeText={(college) => {
								setCollege(college);
								if (name != "" && college != "" && phone != "" && phone.length == 10) {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							className="text-black dark:text-white w-[85%]"
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Enter College Name"
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M11 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h6zM5 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H5z" />
							<Path d="M8 14a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
						</Svg>
						<TextInput
							keyboardType="numeric"
							value={phone}
							onChangeText={(phone) => {
								setPhone(phone);
								if (name != "" && college != "" && phone != "" && phone.length == 10) {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							maxLength={10}
							className="text-black dark:text-white w-[85%]"
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Enter Your Phone"
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" editable={false} onSubmitEditing={Keyboard.dismiss} value={email} placeholder="Enter Your E-Mail" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
				</StyledView>
			</KeyboardAvoidingView>
			<StyledView className={"w-[80%] mx-[10%] mt-0 " + `${Platform.OS === "android" ? "" : "absolute bottom-10"}`}>
				<StyledTouchableOpacity className={"rounded-full w-[80%] mx-[10%] " + `${buttonStatus === "active" ? "bg-[#442c72] dark:bg-[#57309f]" : "bg-[#e3c9ff] dark:bg-[#442c72]"}` + " shadow-xl mb-3"} onPress={submit}>
					<StyledText className="text-center py-3 text-xl font-bold text-white ">Next</StyledText>
				</StyledTouchableOpacity>
			</StyledView>
		</StyledLinearGradient>
	);
}

export default AccountSetup;
