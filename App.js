import React, { useState } from "react";
import { NavigationContainer } from "@react-navigation/native";
import { styled, useColorScheme } from "nativewind";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginChooser from "./Screens/LoginChooser";
import LoginEmail from "./Screens/LoginEmail";
import PasswordRecovery from "./Screens/PasswordRecovery";
import VerificationMethod from "./Screens/VerificationMethod";
import VerificationCode from "./Screens/VerificationCode";
import ResetPassword from "./Screens/ResetPassword";
import Congratulation from "./Screens/Congratulation";
import SignupEmail from "./Screens/SignupEmail";
import AccountSetup from "./Screens/AccountSetup";
import ChooseLocation from "./Screens/ChooseLocation";

const Stack = createNativeStackNavigator();

function App() {
	const { colorScheme, toggleColorScheme } = useColorScheme();
	if (colorScheme == "light") {
		toggleColorScheme;
	}
	return (
		<NavigationContainer>
			<Stack.Navigator>
				<Stack.Screen name="LoginChooser" component={LoginChooser} options={{ headerShown: false }} />
				<Stack.Screen name="LoginEmail" component={LoginEmail} options={{ headerShown: false }} />
				<Stack.Screen name="PasswordRecovery" component={PasswordRecovery} options={{ headerShown: false }} />
				<Stack.Screen name="VerificationMethod" component={VerificationMethod} options={{ headerShown: false }} />
				<Stack.Screen name="VerificationCode" component={VerificationCode} options={{ headerShown: false }} />
				<Stack.Screen name="ResetPassword" component={ResetPassword} options={{ headerShown: false }} />
				<Stack.Screen name="Congratulation" component={Congratulation} options={{ headerShown: false }} />
				<Stack.Screen name="SignupEmail" component={SignupEmail} options={{ headerShown: false }} />
				<Stack.Screen name="AccountSetup" component={AccountSetup} options={{ headerShown: false }} />
				<Stack.Screen name="ChooseLocation" component={ChooseLocation} options={{ headerShown: false }} />
			</Stack.Navigator>
		</NavigationContainer>
	);
}

export default App;
