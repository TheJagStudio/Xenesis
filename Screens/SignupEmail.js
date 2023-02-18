import React, { useState } from "react";
import { Keyboard, Text, View, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView, Platform, Alert } from "react-native";
import { LinearGradient as LG } from "expo-linear-gradient";
import { styled, useColorScheme } from "nativewind";
import Svg, { Circle, Rect, Mask, G, Path, Defs, LinearGradient, Stop } from "react-native-svg";
import AsyncStorage from "@react-native-async-storage/async-storage";
import axios from "axios";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);
const StyledLinearGradient = styled(LG);

function SignupEmail({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [email, setEmail] = useState("");
	const [password1, setPassword1] = useState("");
	const [password2, setPassword2] = useState("");
	const [buttonStatus, setButtonStatus] = useState("inactive");
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
	getData("server", setServer);
	const submit = async () => {
		if (email != "" && password1 != "" && password2 != "" && validate(email) && password1 == password2) {
			saveData("email", email);
			saveData("password", password1);
			var data = JSON.stringify({
				email: email,
				password1: password1,
				password2: password2,
			});
			var config = {
				method: "post",
				maxBodyLength: Infinity,
				url: server + "/api/app/register",
				headers: {
					"Content-Type": "application/json",
				},
				data: data,
			};
			axios(config)
				.then(function (response) {
					let data = response.data;
					navigation.navigate("VerificationCode");
				})
				.catch(function (error) {
					console.log(error);
				});

			//navigation.navigate("VerificationCode");
		} else {
			if (validate(email)) {
				return Alert.alert("Email or Password is not correct");
			} else if (password1 != password2) {
				return Alert.alert("Both Password does not match.");
			} else {
				return Alert.alert("Please enter a valid email.");
			}
		}
	};
	const validate = (text) => {
		let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w\w+)+$/;
		if (reg.test(text) === false) {
			return false;
		} else {
			return true;
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
				<StyledView className="p-5 mx-auto mb-5">
					<Svg width={160} height={160} style={{ shadowColor: "#000000", shadowOpacity: 0.4, shadowRadius: 10 }} viewBox="0 0 158 158" fill="none" xmlns="http://www.w3.org/2000/svg">
						<Circle cx={79} cy={79} r={79} fill="url(#paint0_linear_314_53)" />
						<Rect x={11} y={11} width={136} height={136} rx={10} fill="url(#paint1_linear_314_53)" />
						<Circle cx={79} cy={42} r={17} fill="white" />
						<Mask
							id="mask0_314_53"
							style={{
								maskType: "alpha",
							}}
							maskUnits="userSpaceOnUse"
							x={62}
							y={25}
							width={34}
							height={34}
						>
							<Circle cx={79} cy={42} r={17} fill="white" />
						</Mask>
						<G mask="url(#mask0_314_53)">
							<Path d="M67.25 59C67.25 59 65 59 65 56.75C65 54.5 67.25 47.75 78.5 47.75C89.75 47.75 92 54.5 92 56.75C92 59 89.75 59 89.75 59H67.25ZM78.5 45.5C80.2902 45.5 82.0071 44.7888 83.273 43.523C84.5388 42.2571 85.25 40.5402 85.25 38.75C85.25 36.9598 84.5388 35.2429 83.273 33.977C82.0071 32.7112 80.2902 32 78.5 32C76.7098 32 74.9929 32.7112 73.727 33.977C72.4612 35.2429 71.75 36.9598 71.75 38.75C71.75 40.5402 72.4612 42.2571 73.727 43.523C74.9929 44.7888 76.7098 45.5 78.5 45.5Z" fill="#01008A" />
						</G>
						<Rect x={31} y={68} width={96} height={17} rx={2} fill="white" />
						<Rect x={31} y={94} width={96} height={17} rx={2} fill="white" />
						<Rect x={37} y={73} width={45} height={7} rx={1} fill="#01008A" />
						<Rect x={37} y={98} width={7} height={7} rx={3.5} fill="#01008A" />
						<Rect x={45} y={98} width={7} height={7} rx={3.5} fill="#01008A" />
						<Rect x={53} y={98} width={7} height={7} rx={3.5} fill="#01008A" />
						<Rect x={61} y={98} width={7} height={7} rx={3.5} fill="#01008A" />
						<Rect x={69} y={98} width={7} height={7} rx={3.5} fill="#01008A" />
						<Defs>
							<LinearGradient id="paint0_linear_314_53" x1={158} y1={79} x2={5.029e-8} y2={79} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#3838B4" />
								<Stop offset={1} stopColor="#171793" />
							</LinearGradient>
							<LinearGradient id="paint1_linear_314_53" x1={147} y1={79} x2={11} y2={79} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#FECC6D" />
								<Stop offset={1} stopColor="#FFAA11" />
							</LinearGradient>
						</Defs>
					</Svg>
				</StyledView>
				<StyledView className="p-5">
					<StyledText className="text-[#221144] dark:text-white text-4xl font-bold">Let's Get</StyledText>
					<StyledText className="text-[#221144] dark:text-white text-4xl font-bold">Started</StyledText>
				</StyledView>
				<StyledView className="w-[90%] mx-auto mt-3">
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-lg opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
						</Svg>
						<TextInput
							onChangeText={(email) => {
								setEmail(email);
								if (email != "" && password1 != "" && password2 != "") {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							onChange={(email) => {
								setEmail(email);
								if (email != "" && password1 != "" && password2 != "") {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							className="text-black dark:text-white w-[85%]"
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Email"
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-lg opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-x-125 scale-y-90" viewBox="0 0 16 16">
							<Path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z" />
						</Svg>
						<TextInput
							onChangeText={(password1) => {
								setPassword1(password1);
								if (email != "" && password1 != "" && password2 != "") {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							onChange={(password1) => {
								setPassword1(password1);
								if (email != "" && password1 != "" && password2 != "") {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							className="text-black dark:text-white w-[85%]"
							secureTextEntry={true}
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Password"
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-[#e3c9ff] dark:bg-[#442c72] w-full h-10 rounded-lg opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-x-125 scale-y-90" viewBox="0 0 16 16">
							<Path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z" />
						</Svg>
						<TextInput
							onChangeText={(password2) => {
								setPassword2(password2);
								if (email != "" && password1 != "" && password2 != "") {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							onChange={(password2) => {
								setPassword2(password2);
								if (email != "" && password1 != "" && password2 != "") {
									setButtonStatus("active");
								} else {
									setButtonStatus("inactive");
								}
							}}
							className="text-black dark:text-white w-[85%]"
							secureTextEntry={true}
							onSubmitEditing={Keyboard.dismiss}
							placeholder="Re-type Password"
							placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}
						></TextInput>
					</StyledView>
				</StyledView>
				<StyledView className="w-[80%] mx-[10%] mt-0">
					<StyledTouchableOpacity className={"rounded-full w-[80%] mx-[10%] " + `${buttonStatus === "active" ? "bg-[#442c72] dark:bg-[#57309f]" : "bg-[#e3c9ff] dark:bg-[#442c72]"}` + " shadow-xl mb-3"} onPress={submit}>
						<StyledText className="text-center py-3 text-xl font-bold text-white ">Sign up</StyledText>
					</StyledTouchableOpacity>
					<StyledView className="flex flex-row w-full items-center justify-center">
						<StyledText className=" text-gray-500 text-md">Do you have a account?</StyledText>
						<StyledTouchableOpacity onPress={() => navigation.navigate("LoginEmail")} className="w-fit items-center ml-2">
							<StyledText className=" text-[#211E60] dark:text-white text-md">Login</StyledText>
						</StyledTouchableOpacity>
					</StyledView>
					<StyledView className="w-full items-center justify-center mt-3">
						<StyledText className="text-gray-500">By continuing you agree Xenesis's Terms of</StyledText>
						<StyledText className="text-gray-500">Services & Privay Policy</StyledText>
					</StyledView>
				</StyledView>
			</KeyboardAvoidingView>
		</StyledLinearGradient>
	);
}

export default SignupEmail;
