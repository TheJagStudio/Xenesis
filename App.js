import React, { useState } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { styled, useColorScheme } from "nativewind";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginChooser from "./Screens/LoginChooser";
import LoginEmail from "./Screens/LoginEmail";
import PasswordRecovery from "./Screens/PasswordRecovery";
import VerificationCode from "./Screens/VerificationCode";
import VerificationCodePasswordRecovery from "./Screens/VerificationCodePasswordRecovery";
import ResetPassword from "./Screens/ResetPassword";
import Congratulation from "./Screens/Congratulation";
import SignupEmail from "./Screens/SignupEmail";
import AccountSetup from "./Screens/AccountSetup";
import ChooseLocation from "./Screens/ChooseLocation";
import AsyncStorage from "@react-native-async-storage/async-storage";
import Home from "./Screens/Home";
import Explore from "./Screens/Explore";
import Favorites from "./Screens/Favorites";
import Tickets from "./Screens/Tickets";
import Profile from "./Screens/Profile";
import EventDetails from "./Screens/EventDetails";
import Cart from "./Screens/Cart";

const Stack = createNativeStackNavigator();

function App() {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	const saveData = async (key, value) => {
		try {
			await AsyncStorage.setItem(key, value);
		} catch (error) {
			console.error(error);
		}
	};

	saveData("server", "http://192.168.1.12:8080");
	if (colorScheme == "light") {
		toggleColorScheme;
	}
	return (
		<NavigationContainer>
			<Stack.Navigator>
				<Stack.Screen name="LoginChooser" component={LoginChooser} options={{ headerShown: false }} />
				<Stack.Screen name="LoginEmail" component={LoginEmail} options={{ headerShown: false }} />
				<Stack.Screen name="PasswordRecovery" component={PasswordRecovery} options={{ headerShown: false }} />
				<Stack.Screen name="VerificationCode" component={VerificationCode} options={{ headerShown: false }} />
				<Stack.Screen name="VerificationCodePasswordRecovery" component={VerificationCodePasswordRecovery} options={{ headerShown: false }} />
				<Stack.Screen name="ResetPassword" component={ResetPassword} options={{ headerShown: false }} />
				<Stack.Screen name="Congratulation" component={Congratulation} options={{ headerShown: false }} />
				<Stack.Screen name="SignupEmail" component={SignupEmail} options={{ headerShown: false }} />
				<Stack.Screen name="AccountSetup" component={AccountSetup} options={{ headerShown: false }} />
				<Stack.Screen name="ChooseLocation" component={ChooseLocation} options={{ headerShown: false }} />
				<Stack.Screen name="Home" component={Home} options={{ headerShown: false }} />
				<Stack.Screen name="Explore" component={Explore} options={{ headerShown: false }} />
				<Stack.Screen name="Favorites" component={Favorites} options={{ headerShown: false }} />
				<Stack.Screen name="Tickets" component={Tickets} options={{ headerShown: false }} />
				<Stack.Screen name="Profile" component={Profile} options={{ headerShown: false }} />
				<Stack.Screen name="EventDetails" component={EventDetails} options={{ headerShown: false }} />
				<Stack.Screen name="Cart" component={Cart} options={{ headerShown: false }} />
			</Stack.Navigator>
		</NavigationContainer>
	);
}

export default App;
