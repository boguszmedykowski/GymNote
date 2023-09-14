import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:gymnote/api.dart' as api;

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextEditingController emailController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  Future<void> loginUser(BuildContext context) async {
    final String email = emailController.text;
    final String password = passwordController.text;

    final Map<String, String> data = {
      'email': email,
      'password': password,
    };

    final Uri url = Uri.parse(api.getToken);

    final response = await http.post(
      url,
      body: jsonEncode(data),
      headers: {'Content-Type': 'application/json'},
    );

    if (response.statusCode == 200) {
      // Użytkownik został pomyślnie zalogowany
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: const Text('Sukces'),
            content: const Text('Użytkownik został zalogowany.'),
            actions: <Widget>[
              TextButton(
                child: const Text('OK'),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
            ],
          );
        },
      );

      // Zapisz token API w pamięci urządzenia
      final jsonResponse = json.decode(response.body);
      final token = jsonResponse['token'];
      final preferences = await SharedPreferences.getInstance();
      preferences.setString('apiToken', token);

      // Przejdź do następnego ekranu lub wykonaj inne czynności
    } else {
      // Obsługa błędu logowania
      // Możesz tutaj dodać odpowiednie komunikaty dla użytkownika lub inne działania w przypadku błędu.
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: emailController,
              decoration: const InputDecoration(
                labelText: 'Email',
              ),
            ),
            const SizedBox(height: 16.0),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(
                labelText: 'Password',
              ),
              obscureText: true,
            ),
            const SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () =>
                  loginUser(context), // Wywołanie funkcji loginUser
              child: const Text('Zaloguj'),
            ),
          ],
        ),
      ),
    );
  }
}
