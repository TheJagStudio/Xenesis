import React, { useState } from "react";
import { Keyboard, Text, View, TouchableOpacity, TextInput, SafeAreaView, KeyboardAvoidingView, Platform, Button } from "react-native";
import { styled, useColorScheme } from "nativewind";
import Svg, { Circle, Rect, Mask, G, Path, Defs, LinearGradient, Stop } from "react-native-svg";

const StyledTouchableOpacity = styled(TouchableOpacity);
const StyledText = styled(Text);
const StyledView = styled(View);

function VerificationMethod({ navigation }) {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const [method, setMethod] = useState(true);
	return (
		<SafeAreaView className="bg-white dark:bg-[#221144] h-full" style={{ paddingTop: 40 }}>
			<StyledTouchableOpacity onPress={toggleColorScheme} className="absolute top-10 right-6 z-50">
				<StyledText selectable={false} className="dark:text-white text-3xl">
					{`${colorScheme === "dark" ? "🌙" : "🌞"}`}
				</StyledText>
			</StyledTouchableOpacity>
			<StyledView className="p-3 bg-white dark:bg-[#221144]  z-40 shadow-lg" style={{ shadowColor: Platform.OS === "android" ? "#000000" : "#00000010" }}>
				<StyledTouchableOpacity onPress={() => navigation.navigate("PasswordRecovery")} className="w-[30px] h-[30px] items-center">
					<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#221144"}`} viewBox="0 0 16 16">
						<Path fillRule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2zm11.5 5.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z" />
					</Svg>
				</StyledTouchableOpacity>
				<StyledView className="bg-white dark:bg-[#221144] absolute top-0 h-96 -translate-y-96 w-screen origin-top"></StyledView>
			</StyledView>
			<KeyboardAvoidingView behavior="position">
				<StyledView className="p-5 mx-auto mb-5">
					<Svg width={170} height={170} style={{ shadowColor: "#000000", shadowOpacity: 0.4, shadowRadius: 10 }} viewBox="0 0 170 170" fill="none" xmlns="http://www.w3.org/2000/svg">
						<Circle cx={79} cy={86.8668} r={79} fill="url(#paint0_linear_326_105)" />
						<G filter="url(#filter0_d_326_105)">
							<Path d="M5.17853 50.0747C3.64852 45.9298 5.76831 41.3294 9.91322 39.7994L93.4065 8.97951C97.5515 7.4495 102.152 9.5693 103.682 13.7142L144.544 124.413C146.074 128.558 143.954 133.159 139.809 134.689L56.3162 165.508C52.1713 167.038 47.5708 164.919 46.0408 160.774L5.17853 50.0747Z" fill="url(#paint1_linear_326_105)" />
						</G>
						<G filter="url(#filter1_d_326_105)">
							<Path d="M24 24.8668C24 20.4485 27.5817 16.8668 32 16.8668H82C110.167 16.8668 133 39.7002 133 67.8668V147.867C133 152.285 129.418 155.867 125 155.867H32C27.5817 155.867 24 152.285 24 147.867V24.8668Z" fill="url(#paint2_linear_326_105)" />
						</G>
						<Path d="M81 16.8668H100V25.8668H81V16.8668Z" fill="url(#paint3_linear_326_105)" />
						<Path d="M124 66.8668L124 43.8668L133 43.8668L133 66.8668L124 66.8668Z" fill="url(#paint4_linear_326_105)" />
						<Mask id="mask0_326_105" style={{ maskType: "alpha" }} maskUnits="userSpaceOnUse" x={94} y={12} width={46} height={46}>
							<Path d="M94.0177 57.9302L94.0173 12.0113L139.04 48.9023L94.0177 57.9302Z" fill="#D9D9D9" />
						</Mask>
						<G mask="url(#mask0_326_105)">
							<G filter="url(#filter2_d_326_105)">
								<Path d="M99.999 16.8663H132.999V43.8663H104.999C102.238 43.8663 99.999 41.6278 99.999 38.8663V16.8663Z" fill="white" />
							</G>
						</G>
						<Rect x={36} y={29.8668} width={70} height={4} rx={2} fill="white" />
						<Rect x={36} y={41.8668} width={51} height={4} rx={2} fill="white" />
						<Rect x={36} y={59.8668} width={86} height={4} rx={2} fill="white" />
						<Rect x={36} y={68.8668} width={86} height={4} rx={2} fill="white" />
						<Rect x={36} y={77.8668} width={86} height={4} rx={2} fill="white" />
						<Rect x={36} y={86.8668} width={33} height={4} rx={2} fill="white" />
						<Rect x={88} y={86.8668} width={33} height={4} rx={2} fill="white" />
						<Rect x={36} y={104.867} width={24} height={4} rx={2} fill="white" />
						<Rect x={36} y={123.867} width={29} height={4} rx={2} fill="white" />
						<Rect x={36} y={113.867} width={70} height={4} rx={2} fill="white" />
						<Rect x={109} y={113.867} width={13} height={4} rx={2} fill="white" />
						<Rect x={70} y={123.867} width={13} height={4} rx={2} fill="white" />
						<Rect x={72} y={86.8668} width={13} height={4} rx={2} fill="white" />
						<Rect x={63} y={104.867} width={59} height={4} rx={2} fill="white" />
						<Rect x={36} y={95.8668} width={78} height={4} rx={2} fill="white" />
						<G filter="url(#filter3_d_326_105)">
							<Circle cx={78.5} cy={86.5} r={29.5} fill="url(#paint5_linear_326_105)" />
						</G>
						<Path
							fillRule="evenodd"
							clipRule="evenodd"
							d="M79 66C77.2257 66 74.2609 66.6791 71.4709 67.435C68.6166 68.2038 65.7392 69.1134 64.0472 69.6644C63.3397 69.8972 62.7126 70.3241 62.2377 70.8962C61.7628 71.4682 61.4595 72.1621 61.3626 72.8982C59.83 84.3706 63.3863 92.8729 67.7012 98.4976C69.5309 100.904 71.7126 103.023 74.1734 104.783C75.166 105.483 76.0866 106.019 76.8683 106.385C77.5883 106.723 78.3623 107 79 107C79.6377 107 80.4091 106.723 81.1317 106.385C82.0741 105.929 82.9757 105.393 83.8266 104.783C86.2874 103.023 88.4691 100.904 90.2988 98.4976C94.6137 92.8729 98.17 84.3706 96.6374 72.8982C96.5407 72.1618 96.2375 71.4675 95.7626 70.895C95.2877 70.3225 94.6605 69.8951 93.9528 69.6618C91.4966 68.8593 89.0213 68.1159 86.5291 67.4324C83.7391 66.6816 80.7743 66 79 66ZM79 78.8125C79.9109 78.8111 80.7929 79.1311 81.4897 79.7157C82.1866 80.3003 82.6534 81.1118 82.8074 82.0064C82.9614 82.9011 82.7926 83.8212 82.3311 84.6038C81.8696 85.3864 81.145 85.981 80.2857 86.2822L81.2757 91.3816C81.3117 91.567 81.3061 91.7581 81.2594 91.9412C81.2126 92.1243 81.1257 92.2948 81.0051 92.4405C80.8844 92.5862 80.7329 92.7035 80.5614 92.784C80.3899 92.8646 80.2027 92.9063 80.0131 92.9062H77.9869C77.7975 92.9059 77.6106 92.8639 77.4394 92.7832C77.2682 92.7025 77.117 92.5852 76.9967 92.4395C76.8763 92.2938 76.7897 92.1235 76.7431 91.9406C76.6964 91.7577 76.6909 91.5668 76.7269 91.3816L77.7143 86.2822C76.855 85.981 76.1304 85.3864 75.6689 84.6038C75.2074 83.8212 75.0386 82.9011 75.1926 82.0064C75.3466 81.1118 75.8134 80.3003 76.5103 79.7157C77.2071 79.1311 78.0891 78.8111 79 78.8125Z"
							fill="white"
						/>
						<Defs>
							<LinearGradient id="paint0_linear_326_105" x1={158} y1={86.8668} x2={5.029e-8} y2={86.8668} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#3838B4" />
								<Stop offset={1} stopColor="#171793" />
							</LinearGradient>
							<LinearGradient id="paint1_linear_326_105" x1={124.113} y1={69.0637} x2={25.6097} y2={105.424} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#FFCC71" />
								<Stop offset={1} stopColor="#FFAC12" />
							</LinearGradient>
							<LinearGradient id="paint2_linear_326_105" x1={133} y1={86.3668} x2={24} y2={86.3668} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#FFCC71" />
								<Stop offset={1} stopColor="#FFAC12" />
							</LinearGradient>
							<LinearGradient id="paint3_linear_326_105" x1={100} y1={20.8668} x2={81} y2={20.8668} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#FEC051" />
								<Stop offset={1} stopColor="#FFBD43" />
							</LinearGradient>
							<LinearGradient id="paint4_linear_326_105" x1={133} y1={54.3668} x2={124} y2={54.3668} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#FFCC71" />
								<Stop offset={1} stopColor="#FFC969" />
							</LinearGradient>
							<LinearGradient id="paint5_linear_326_105" x1={108} y1={86.5} x2={49} y2={86.5} gradientUnits="userSpaceOnUse">
								<Stop stopColor="#3838B4" />
								<Stop offset={1} stopColor="#171793" />
							</LinearGradient>
						</Defs>
					</Svg>
				</StyledView>
				<StyledView className="p-5">
					<StyledText className="text-[#221144] dark:text-white text-4xl font-bold">Verification</StyledText>
					<StyledText className="text-[#221144] dark:text-white text-4xl font-bold">Method</StyledText>
					<StyledText className="text-[#221144] dark:text-white text-sm opacity-50">We'll send you a verification code to reset your password.</StyledText>
				</StyledView>
				<StyledView className="w-[90%] mx-auto mt-3">
					<StyledView className="flex flex-row justify-between items-center bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-80 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<StyledView className="flex flex-row items-center">
							<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
								<Path d="M11 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h6zM5 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H5z" />
								<Path d="M8 14a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
							</Svg>
							<Text className="text-[#221144] dark:text-white">82* *** **50</Text>
						</StyledView>
						<StyledTouchableOpacity
							onPress={() => {
								setMethod(true);
							}}
							className="border-[3px] border-[#221144] dark:border-white w-5 h-5 overflow-hidden rounded-full mr-2"
						>
							<StyledView className={`${method === true ? "block" : "hidden"}` + " w-2.5 h-2.5 rounded-full bg-[#221144] dark:bg-white mt-0.5 ml-0.5"}></StyledView>
						</StyledTouchableOpacity>
					</StyledView>
					<StyledView className="flex flex-row justify-between items-center bg-slate-300 dark:bg-gray-700 w-full h-10 rounded-full opacity-80 focus:opacity-80 shadow-lg p-2 pl-3 mb-3">
						<StyledView className="flex flex-row items-center">
							<Svg xmlns="http://www.w3.org/2000/svg" width={25} height={25} fill={`${colorScheme === "dark" ? "#FFFFFF" : "#000000"}`} className="mr-3 scale-75" viewBox="0 0 16 16">
								<Path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
							</Svg>
							<Text className="text-[#221144] dark:text-white">the*********@gmail.com</Text>
						</StyledView>
						<StyledTouchableOpacity
							onPress={() => {
								setMethod(false);
							}}
							className="border-[3px] border-[#221144] dark:border-white w-5 h-5 overflow-hidden rounded-full mr-2"
						>
							<StyledView className={`${method === false ? "block" : "hidden"}` + " w-2.5 h-2.5 rounded-full bg-[#221144] dark:bg-white mt-0.5 ml-0.5"}></StyledView>
						</StyledTouchableOpacity>
					</StyledView>
				</StyledView>
			</KeyboardAvoidingView>
			<StyledView className="w-[80%] mx-[10%] absolute bottom-10">
				<StyledTouchableOpacity className="rounded-full w-[80%] mx-[10%] bg-[#211E60] shadow-xl mb-3" onPress={() => navigation.navigate("VerificationCode")}>
					<StyledText className="text-center py-3 text-xl font-bold text-white ">Next</StyledText>
				</StyledTouchableOpacity>
			</StyledView>
		</SafeAreaView>
	);
}

export default VerificationMethod;
