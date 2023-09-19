import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:gymnote/api.dart' as api;

class UserWorkoutsPage extends StatefulWidget {
  @override
  _UserWorkoutsPageState createState() => _UserWorkoutsPageState();
}

class _UserWorkoutsPageState extends State<UserWorkoutsPage> {
  List<dynamic> workouts = []; // Lista treningów

  @override
  void initState() {
    super.initState();
    fetchWorkouts(); // Pobierz listę treningów przy inicjalizacji strony
  }

  Future<void> fetchWorkouts() async {
    final headers = await api.getApiHeaders(); // Uzyskaj nagłówki z tokenem API
    final Uri url = Uri.parse(api.getWorkouts);

    final response = await http.get(
      url,
      headers: headers, // Dodaj token jako nagłówek
    );

    if (response.statusCode == 200) {
      // Jeśli odpowiedź jest OK (kod 200), przetwórz dane JSON
      setState(() {
        workouts = json.decode(response.body);
      });
    } else {
      // W przypadku błędu wyświetl komunikat o błędzie
      print('Błąd: ${response.statusCode}');
      print('Treść odpowiedzi: ${response.body}');
      throw Exception('Failed to load workouts');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('User Workouts'),
      ),
      body: ListView.builder(
        itemCount: workouts.length,
        itemBuilder: (context, index) {
          final workout = workouts[index];
          return ListTile(
            title: Text(workout['title'] ?? ''),
            subtitle: Text(workout['link'] ?? ''),
            // Możesz dodać więcej informacji o treningu, jeśli są dostępne
          );
        },
      ),
    );
  }
}

void main() {
  runApp(MaterialApp(
    home: UserWorkoutsPage(),
  ));
}
