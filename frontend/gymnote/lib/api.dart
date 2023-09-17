import 'package:shared_preferences/shared_preferences.dart';

const baseURL = 'http://127.0.0.1';

const register = '$baseURL/api/user/create/';
const getToken = '$baseURL/api/user/token/';
const getWorkouts = '$baseURL/api/note/workouts/';

Future<Map<String, String>> getApiHeaders() async {
  final Map<String, String> headers = {};

  final preferences = await SharedPreferences.getInstance();
  final token = preferences.getString('apiToken');

  if (token != null) {
    headers['Authorization'] = 'Token $token';
  }

  return headers;
}
