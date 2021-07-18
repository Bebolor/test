from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bracket.models import Bracket
from bracket.serializers import BracketSerializer
from match.serializers import MatchSerializer
from round.serializers import RoundSerializer
from tournament.models import Tournament
from tournament.serializers.serializers import CreateTournamentSerializer, ListTournamentSerializer

User = get_user_model()


def participants_shuffle(array):
    new_array = [array[0], *array[2:], array[1]]
    return new_array


class ListTournamentView(ListAPIView):
    # permission_classes = []
    queryset = Tournament.objects.all()
    serializer_class = ListTournamentSerializer


class CreateTournamentView(CreateAPIView):
    serializer_class = CreateTournamentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organizer=request.user)
        participants = []
        for i in range(0, serializer.data["no_of_players"]):
            participants.append({"first_name": "Player", "last_name": i + 1})
        bracket_data = {"tournament": serializer.data["id"]}
        bracket_serializer = BracketSerializer(data=bracket_data)
        bracket_serializer.is_valid(raise_exception=True)
        bracket_serializer.save()
        if serializer.data["format"] == "RR":
            if (len(participants) % 2) == 0:
                for i in range(0, len(participants) - 1):
                    round_data = {"bracket": bracket_serializer.data}
                    round_serializer = RoundSerializer(data=round_data)
                    round_serializer.is_valid(raise_exception=True)
                    round_serializer.save(bracket_id=bracket_serializer.data["id"])
                    for j in range(0, int(len(participants) / 2)):
                        match_data = {"round": round_serializer.data["id"],
                                      "mock_players": [participants[j], participants[len(participants) - 1 - j]]}
                        match_serializer = MatchSerializer(data=match_data)
                        match_serializer.is_valid(raise_exception=True)
                        match_serializer.save()
                    participants = participants_shuffle(participants)
            else:
                participants.append({"first_name": "BYE", "last_name": ""})
                for i in range(0, len(participants)):
                    round_data = {"bracket": bracket_serializer.data}
                    round_serializer = RoundSerializer(data=round_data)
                    round_serializer.is_valid(raise_exception=True)
                    round_serializer.save(bracket_id=bracket_serializer.data["id"])
                    for j in range(0, int(len(participants) / 2)):
                        match_data = {"round": round_serializer.data["id"],
                                      "mock_players": [participants[j], participants[len(participants) - 1 - j]]}
                        match_serializer = MatchSerializer(data=match_data)
                        match_serializer.is_valid(raise_exception=True)
                        match_serializer.save()
                    participants = participants_shuffle(participants)
        elif serializer.data["format"] == "SE":
            nr_of_rounds = 0
            while len(participants) > pow(2, nr_of_rounds):
                nr_of_rounds += 1
            nr_of_bye = pow(2, nr_of_rounds) - len(participants)
            participants_first_round = len(participants) - nr_of_bye
            for i in range(nr_of_rounds, 0, -1):
                round_data = {"bracket": bracket_serializer.data}
                round_serializer = RoundSerializer(data=round_data)
                round_serializer.is_valid(raise_exception=True)
                round_serializer.save(bracket_id=bracket_serializer.data["id"])
                if i == nr_of_rounds:
                    if nr_of_bye == 0:
                        for j in range(0, pow(2, i), 2):
                            match_data = {"round": round_serializer.data["id"],
                                          "mock_players": [participants[j], participants[j + 1]]}
                            match_serializer = MatchSerializer(data=match_data)
                            match_serializer.is_valid(raise_exception=True)
                            match_serializer.save()
                    else:
                        for j in range(0, participants_first_round, 2):
                            match_data = {"round": round_serializer.data["id"],
                                          "mock_players": [participants[j], participants[j + 1]]}
                            match_serializer = MatchSerializer(data=match_data)
                            match_serializer.is_valid(raise_exception=True)
                            match_serializer.save()
                        for j in range(0, nr_of_bye):
                            match_data = {"round": round_serializer.data["id"]}
                            match_serializer = MatchSerializer(data=match_data)
                            match_serializer.is_valid(raise_exception=True)
                            match_serializer.save()
                elif i == nr_of_rounds - 1:
                    if nr_of_bye == 0:
                        for j in range(0, pow(2, i), 2):
                            match_data = {"round": round_serializer.data["id"],
                                          "mock_players": [{"first_name": "Winner", "last_name": ""}, {"first_name": "Winner", "last_name": ""}]}
                            match_serializer = MatchSerializer(data=match_data)
                            match_serializer.is_valid(raise_exception=True)
                            match_serializer.save()
                    else:
                        for j in range(0, int(participants_first_round / 4)):
                            match_data = {"round": round_serializer.data["id"],
                                          "mock_players": [{"first_name": "Winner", "last_name": ""}, {"first_name": "Winner", "last_name": ""}]}
                            match_serializer = MatchSerializer(data=match_data)
                            match_serializer.is_valid(raise_exception=True)
                            match_serializer.save()
                        if nr_of_bye % 2 == 0:
                            for j in range(participants_first_round, len(participants), 2):
                                print(j)
                                match_data = {"round": round_serializer.data["id"],
                                              "mock_players": [participants[j], participants[j + 1]]}
                                match_serializer = MatchSerializer(data=match_data)
                                match_serializer.is_valid(raise_exception=True)
                                match_serializer.save()
                        else:
                            match_data = {"round": round_serializer.data["id"],
                                          "mock_players": [{"first_name": "Winner", "last_name": ""}, participants[participants_first_round]]}
                            match_serializer = MatchSerializer(data=match_data)
                            match_serializer.is_valid(raise_exception=True)
                            match_serializer.save()
                            for j in range(participants_first_round + 1, pow(2, i), 2):
                                match_data = {"round": round_serializer.data["id"],
                                              "mock_players": [participants[j], participants[j + 1]]}
                                match_serializer = MatchSerializer(data=match_data)
                                match_serializer.is_valid(raise_exception=True)
                                match_serializer.save()
                else:
                    for j in range(0, pow(2, i), 2):
                        match_data = {"round": round_serializer.data["id"],
                                      "mock_players": [{"first_name": "Winner", "last_name": ""}, {"first_name": "Winner", "last_name": ""}]}
                        match_serializer = MatchSerializer(data=match_data)
                        match_serializer.is_valid(raise_exception=True)
                        match_serializer.save()
        return Response(serializer.data)


class RetrieveUpdateDestroyTournamentView(RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = ListTournamentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        try:
            if request.data["status"] == "OG":
                bracket = Bracket.objects.get(tournament=kwargs["pk"])
                bracket.delete()
                tournament = self.get_object()
                participants = tournament.participants.all()
                bracket_data = {"tournament": tournament.id}
                bracket_serializer = BracketSerializer(data=bracket_data)
                bracket_serializer.is_valid(raise_exception=True)
                bracket_serializer.save()
                if tournament.format == "RR":
                    if (len(participants) % 2) == 0:
                        for i in range(0, len(participants) - 1):
                            round_data = {"bracket": bracket_serializer.data}
                            round_serializer = RoundSerializer(data=round_data)
                            round_serializer.is_valid(raise_exception=True)
                            round_serializer.save(bracket_id=bracket_serializer.data["id"])
                            for j in range(0, int(len(participants) / 2)):
                                match_data = {"round": round_serializer.data["id"]}
                                match_serializer = MatchSerializer(data=match_data)
                                match_serializer.is_valid(raise_exception=True)
                                match_serializer.save(players=[participants[j], participants[len(participants) - 1 - j]])
                            participants = participants_shuffle(participants)
                    else:
                        participants.append({"first_name": "BYE", "last_name": ""})
                        for i in range(0, len(participants)):
                            round_data = {"bracket": bracket_serializer.data}
                            round_serializer = RoundSerializer(data=round_data)
                            round_serializer.is_valid(raise_exception=True)
                            round_serializer.save(bracket_id=bracket_serializer.data["id"])
                            for j in range(0, int(len(participants) / 2)):
                                match_data = {"round": round_serializer.data["id"]}
                                match_serializer = MatchSerializer(data=match_data)
                                match_serializer.is_valid(raise_exception=True)
                                match_serializer.save(players=[participants[j], participants[len(participants) - 1 - j]])
                            participants = participants_shuffle(participants)
            return self.partial_update(request, *args, **kwargs)
        except KeyError:
            return self.partial_update(request, *args, **kwargs)
