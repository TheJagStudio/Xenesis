import React from "react";
import { Text, View, TouchableOpacity, Image } from "react-native";
import { styled, useColorScheme } from "nativewind";
import Swiper from "react-native-swiper";
const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);

function LoginChooser({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	return (
		<StyledView className="h-full justify-center bg-white dark:bg-[#28272C] transition-[background] duration-300">
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<Swiper showsButtons={false} loop={true} autoplay={true} autoplayTimeout={5} bounces={true} activeDotColor={"#FEA500"}>
				<StyledView className="w-full h-[120vw]">
					<Image className="w-full h-full -translate-y-10" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} resizeMode="contain" source={require("../assets/loading1.png")}></Image>
					<StyledText className="text-4xl font-bold ml-[10%] dark:text-white">Enjoy your life</StyledText>
				</StyledView>
				<StyledView className="w-full h-[120vw]">
					<Image className="w-full h-full -translate-y-10" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} resizeMode="contain" source={require("../assets/loading2.png")}></Image>
					<StyledText className="text-4xl font-bold ml-[10%] dark:text-white">Enjoy Xenesis</StyledText>
				</StyledView>
				<StyledView className="w-full h-[120vw]">
					<Image className="w-full h-full -translate-y-10" style={{ shadowColor: "#000000", shadowOpacity: 0.5, shadowRadius: 10 }} resizeMode="contain" source={require("../assets/loading3.png")}></Image>
					<StyledText className="text-4xl font-bold ml-[10%] dark:text-white">Enjoy this world</StyledText>
				</StyledView>
			</Swiper>
			<StyledView className="w-[80%] mx-[10%] absolute bottom-0 mb-24">
				<StyledTouchableOpacity className="rounded-full w-full bg-[#FEA500] shadow-xl mb-3" onPress={() => navigation.navigate("LoginEmail")}>
					<StyledText className="text-center py-3 text-xl font-bold text-white ">Continue with Email</StyledText>
				</StyledTouchableOpacity>
				<StyledView className="flex flex-row gap-2">
					<StyledTouchableOpacity className="rounded-full w-[47.5%] border border-[#28272C] dark:border-white py-2 items-center justify-center">
						<Image style={{ width: 20, height: 20 }} source={require("../assets/google.png")}></Image>
					</StyledTouchableOpacity>
					<StyledTouchableOpacity className="rounded-full w-[47.5%] border border-[#28272C] dark:border-white py-2 items-center justify-center">
						<Image style={{ width: 20, height: 20 }} source={require("../assets/facebook.png")}></Image>
					</StyledTouchableOpacity>
				</StyledView>
				<StyledView className="w-full items-center justify-center mt-3">
					<StyledText className="text-gray-500">By continuing you agree Xenesis's Terms of</StyledText>
					<StyledText className="text-gray-500">Services & Privay Policy</StyledText>
				</StyledView>
			</StyledView>
		</StyledView>
	);
}

export default LoginChooser;
