import React from "react";
import { Keyboard, Text, View, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView, Platform } from "react-native";
import { styled, useColorScheme } from "nativewind";
import Svg, { Circle, Rect, Mask, G, Path, Defs, LinearGradient, Stop } from "react-native-svg";
const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);

function SignupEmail({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	return (
		<SafeAreaView className="bg-white dark:bg-[#28272C] h-full" style={{ paddingTop: Platform.OS === "android" ? 40 : 0 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-6 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="p-3">
				<StyledTouchableOpacity onPress={() => navigation.navigate("LoginEmail")} className="w-[30px] h-[30px] items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#28272C"}`} viewBox="0 0 16 16">
						<Path fillRule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
					</Svg>
				</StyledTouchableOpacity>
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
					<StyledText className="text-[#28272C] dark:text-white text-4xl font-bold">Let's Get</StyledText>
					<StyledText className="text-[#28272C] dark:text-white text-4xl font-bold">Started</StyledText>
				</StyledView>
				<StyledView className="w-[90%] mx-auto mt-3">
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} placeholder="Email" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-x-125 scale-y-90" viewBox="0 0 16 16">
							<Path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} placeholder="Password" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-x-125 scale-y-90" viewBox="0 0 16 16">
							<Path d="M8 1a2 2 0 0 1 2 2v4H6V3a2 2 0 0 1 2-2zm3 6V3a3 3 0 0 0-6 0v4a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM5 8h6a1 1 0 0 1 1 1v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} placeholder="Re-type Password" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
				</StyledView>
				<StyledView className="w-[80%] mx-[10%] mt-0">
					<StyledTouchableOpacity className="rounded-full w-[80%] mx-[10%] bg-[#FEA500] shadow-xl mb-3" onPress={() => navigation.navigate("LoginEmail")}>
						<StyledText className="text-center py-3 text-xl font-bold text-white ">Sign up</StyledText>
					</StyledTouchableOpacity>
					<StyledView className="flex flex-row w-full items-center justify-center">
						<StyledText className=" text-gray-500 text-md">Do you have a account?</StyledText>
						<StyledTouchableOpacity onPress={() => navigation.navigate("LoginEmail")} className="w-fit items-center ml-2">
							<StyledText className=" text-[#FEA500] text-md">Login</StyledText>
						</StyledTouchableOpacity>
					</StyledView>
					<StyledView className="w-full items-center justify-center mt-3">
						<StyledText className="text-gray-500">By continuing you agree Xenesis's Terms of</StyledText>
						<StyledText className="text-gray-500">Services & Privay Policy</StyledText>
					</StyledView>
				</StyledView>
			</KeyboardAvoidingView>
		</SafeAreaView>
	);
}

export default SignupEmail;
