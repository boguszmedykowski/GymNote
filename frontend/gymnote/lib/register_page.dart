import 'dart:convert' show jsonEncode;
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:gymnote/api.dart' as api;

class RegisterPage extends StatelessWidget {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final TextEditingController confirmPasswordController =
      TextEditingController();

  RegisterPage({super.key});

  Future<void> registerUser(BuildContext context) async {
    final String email = emailController.text;
    final String password = passwordController.text;
    final String confirmPassword = confirmPasswordController.text;

    // Sprawdź, czy hasła są takie same
    if (password != confirmPassword) {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: const Text('Błąd'),
            content: const Text('Hasła nie pasują do siebie.'),
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
      return;
    }

    final Map<String, String> data = {
      'email': email,
      'password': password,
    };

    final Uri url = Uri.parse(api.register);

    final response = await http.post(
      url,
      body: jsonEncode(data),
      headers: {'Content-Type': 'application/json'},
    );

    if (response.statusCode == 201) {
      // Użytkownik został pomyślnie zarejestrowany
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: const Text('Sukces'),
            content: const Text('Użytkownik został zarejestrowany.'),
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
    } else {
      // Wystąpił błąd podczas rejestracji użytkownika
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: const Text('Błąd'),
            content:
                const Text('Wystąpił błąd podczas rejestracji użytkownika.'),
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
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Rejestracja'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              controller: emailController,
              decoration: const InputDecoration(
                labelText: 'Email',
              ),
            ),
            const SizedBox(height: 8.0),
            TextField(
              controller: passwordController,
              decoration: const InputDecoration(
                labelText: 'Hasło',
              ),
              obscureText: true,
            ),
            const SizedBox(height: 8.0),
            TextField(
              controller: confirmPasswordController,
              decoration: const InputDecoration(
                labelText: 'Powtórz hasło',
              ),
              obscureText: true,
            ),
            const SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: () => registerUser(context),
              child: const Text('Zarejestruj się'),
            ),
          ],
        ),
      ),
    );
  }
}
