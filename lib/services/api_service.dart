import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

class ApiService {
  static const String _baseUrl = 'http://192.122.31.12:5000';

  static Future<List<dynamic>> detectObjects(File imageFile) async {
    var request = http.MultipartRequest('POST', Uri.parse('$_baseUrl/predict'));

    request.files.add(
      await http.MultipartFile.fromPath('image', imageFile.path),
    );

    var streamedResponse = await request.send();
    var response = await http.Response.fromStream(streamedResponse);

    if (response.statusCode == 200) {
      print("✅ ${response.body}");
      return jsonDecode(response.body);
    } else {
      throw Exception(
        'Failed to detect objects. Status code: ${response.statusCode}',
      );
    }
  }
}
