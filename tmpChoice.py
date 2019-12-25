# <!--<form action="{% url 'polls:vote' question.id %}" method="post">-->
# <!--{% csrf_token %}-->
# <!--{% for good in question.choice_set.all %}-->
# <!--    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">-->
# <!--    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>-->
# <!--{% endfor %}-->
# <!--<input type="submit" value="Vote">-->
# <!--</form>-->


# <button style="border: 0; padding: 0; background: white" onclick="myFunction()">