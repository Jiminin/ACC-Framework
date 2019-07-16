<h1>{{race_name}}</h1>
<form method="post" action="/race">
  <div>
    <label for="track">Rata missä hurjastellaan:</label>
    <select name="track" id="track">
      % for track in track_list:
      <!-- Palautetaan radan ID arvo, ei nimeä! -->
        <option value="{{track['id']}}">{{track['name']}}</option>
      % end
    </select>
  </div>
  <div>
    <label for="weather">Sää ennuste numeroina: </label>
    <input name="weather" type="text" />
  </div>
  <p>
  </p>
  <button type="submit">Lähetä tiedot eteenpäin!</button>
</form>