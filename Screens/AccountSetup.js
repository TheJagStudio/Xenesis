import React, { useState } from "react";
import { Keyboard, Text, View, Image, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView, Platform } from "react-native";
import { styled, useColorScheme } from "nativewind";
import Svg, { Path } from "react-native-svg";
import Swiper from "react-native-swiper";
const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);

function AccountSetup({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [avatarId, setAvatarId] = useState("0001");
	const [imageAnim, setImageAnim] = useState(false);
	const [imageCover, setImageCover] = useState(false);
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
				<StyledTouchableOpacity
					className="mx-auto mb-5 h-32 w-32 bg-gray-300 dark:bg-gray-700 rounded-full overflow-hidden"
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
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3" viewBox="0 0 16 16">
							<Path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} placeholder="Full Name" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} placeholder="Enter Your Birthday" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M11 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h6zM5 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H5z" />
							<Path d="M8 14a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} placeholder="Enter Your Phone" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
					<StyledView className="flex flex-row group bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-50 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
							<Path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
						</Svg>
						<TextInput className="text-black dark:text-white w-[85%]" onSubmitEditing={Keyboard.dismiss} value={"thejagstudio@gmail.com"} placeholder="Enter Your E-Mail" placeholderTextColor={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`}></TextInput>
					</StyledView>
				</StyledView>
			</KeyboardAvoidingView>
			<StyledView className="w-[80%] mx-[10%] mt-0 absolute bottom-10">
				<StyledTouchableOpacity className="rounded-full w-[80%] mx-[10%] bg-[#FEA500] shadow-xl mb-3" onPress={() => navigation.navigate("ChooseLocation")}>
					<StyledText className="text-center py-3 text-xl font-bold text-white ">Next</StyledText>
				</StyledTouchableOpacity>
			</StyledView>
		</SafeAreaView>
	);
}

export default AccountSetup;
